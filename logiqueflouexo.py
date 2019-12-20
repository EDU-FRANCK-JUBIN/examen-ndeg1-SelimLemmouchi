import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

error = ctrl.Antecedent(np.arange(-4, 4, 1), 'error')
errordot = ctrl.Antecedent(np.arange(-10, 10, 1), 'errordot')
percent = ctrl.Consequent(np.arange(-101, 101, 1), 'percent')

error['toohot'] = fuzz.trimf(error.universe, [-4, -2, 0])
error['justright'] = fuzz.trimf(error.universe, [-2, 0, 2])
error['toocold'] = fuzz.trimf(error.universe, [0, 2, 4])

errordot['gettinghotter'] = fuzz.trimf(errordot.universe, [-10, -5, 0])
errordot['nochange'] = fuzz.trimf(errordot.universe, [-5, 0, 5])
errordot['gettingcolder'] = fuzz.trimf(errordot.universe, [0, 5, 10])

percent['cool'] = fuzz.trimf(percent.universe, [-100, -50, 0])
percent['donothing'] = fuzz.trimf(percent.universe, [-50, 0, 50])
percent['heat'] = fuzz.trimf(percent.universe, [0, 50, 100])

ruleCool1 = ctrl.Rule(error['toohot'] | errordot['gettingcolder'], percent['cool'])
ruleCool2 = ctrl.Rule(error['toohot'] | errordot['nochange'], percent['cool'])
ruleCool3 = ctrl.Rule(error['toohot'] | errordot['gettinghotter'], percent['cool'])
ruleCool4 = ctrl.Rule(error['justright'] | errordot['gettingcolder'], percent['cool'])
ruleHeat1 = ctrl.Rule(error['justright'] | errordot['gettingcolder'], percent['heat'])
ruleHeat2 = ctrl.Rule(error['toocold'] | errordot['gettingcolder'], percent['heat'])
ruleHeat3 = ctrl.Rule(error['toocold'] | errordot['nochange'], percent['heat'])
ruleHeat4 = ctrl.Rule(error['toocold'] | errordot['gettinghotter'], percent['heat'])
ruleDoNothing = ctrl.Rule(error['justright'] | errordot['nochange'], percent['donothing'])

percent_ctrl = ctrl.ControlSystem([ruleCool1, ruleCool2, ruleCool3, ruleCool4, ruleDoNothing, ruleHeat1,ruleHeat2, ruleHeat3, ruleHeat4])

percent_check = ctrl.ControlSystemSimulation(percent_ctrl)

percent_check.input['error'] = -1.5
percent_check.input['errordot'] = -4
percent_check.compute()

print(percent_check.output['percent'])

percent_check.input['error'] = -1.5
percent_check.input['errordot'] = -1
percent_check.compute()

print(percent_check.output['percent'])

percent_check.input['error'] = 0.5
percent_check.input['errordot'] = 1
percent_check.compute()

print(percent_check.output['percent'])

percent_check.input['error'] = 0.5
percent_check.input['errordot'] = 4
percent_check.compute()

print(percent_check.output['percent'])

