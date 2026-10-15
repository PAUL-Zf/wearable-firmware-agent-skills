"""Meaningful regression cases for firmware helper corrections and non-overwriting installation."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[1]

class ToolTests(unittest.TestCase):
    def run_tool(self, script, *args):
        return subprocess.run([sys.executable, str(ROOT/script), *map(str,args)], text=True, capture_output=True)
    def test_ble_valid_and_strict_invalid_combinations(self):
        script='skills/zephyr-connectivity-ble/scripts/ble_timing_helper.py'
        self.assertEqual(self.run_tool(script,'--conn-ms','100','--latency','4','--timeout-ms','4000').returncode,0)
        for timeout in ['10000','24000']:
            self.assertNotEqual(self.run_tool(script,'--conn-ms','2000','--latency','5','--timeout-ms',timeout).returncode,0)
    def test_ble_rejects_nonfinite_range_and_unrepresentable(self):
        script='skills/zephyr-connectivity-ble/scripts/ble_timing_helper.py'
        for value in ['nan','inf','-1','5000','7.6']:
            self.assertNotEqual(self.run_tool(script,'--conn-ms',value).returncode,0)
    def test_power_budget_and_invalid_models(self):
        script='skills/zephyr-power-performance/scripts/power_budget_estimator.py'
        with tempfile.TemporaryDirectory() as d:
            csv=Path(d)/'budget.csv'
            csv.write_text('state,current_ma,duty_cycle_percent\nactive,10,10\nsleep,0,90\n')
            result=self.run_tool(script,'--csv',csv,'--battery-mah','100')
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertIn('100.00 h',result.stdout)
            for capacity in ['0','-1','nan','inf']:
                self.assertNotEqual(self.run_tool(script,'--csv',csv,'--battery-mah',capacity).returncode,0)
            for bad in ['active,nan,100','active,1,nan','active,1,50','active,-1,100']:
                csv.write_text('state,current_ma,duty_cycle_percent\n'+bad+'\n')
                self.assertNotEqual(self.run_tool(script,'--csv',csv,'--battery-mah','100').returncode,0)
    def test_installer_preserves_provenance_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            script='scripts/install_skills.py'
            result=self.run_tool(script,'--dest',d,'c-pro')
            self.assertEqual(result.returncode,0,result.stderr)
            for f in ['SKILL.md','LICENSE','SOURCE.json']:
                self.assertTrue((Path(d)/'c-pro'/f).is_file())
            source=json.loads((Path(d)/'c-pro/SOURCE.json').read_text())
            self.assertEqual(source['name'],'c-pro')
            self.assertNotEqual(self.run_tool(script,'--dest',d,'c-pro').returncode,0)
    def test_installer_resolves_cmsis_and_local_links(self):
        with tempfile.TemporaryDirectory() as d:
            result=self.run_tool('scripts/install_skills.py','--dest',d,'cmsis-debug-live')
            self.assertEqual(result.returncode,0,result.stderr)
            for name in ['cmsis-debug-live','debug-access-knowledge','check-cmsis-environment','cmsis-debugger-setup']:
                self.assertTrue((Path(d)/name/'SKILL.md').is_file())

if __name__=='__main__':
    unittest.main()
