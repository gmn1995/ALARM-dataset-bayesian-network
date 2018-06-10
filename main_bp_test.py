from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianModel
from pgmpy.inference import BeliefPropagation

bayesian_model = BayesianModel([('A', 'J'), ('R', 'J'), ('J', 'Q'),('J', 'L'), ('G', 'L')]);
cpd_a = TabularCPD('A', 2, [[0.2], [0.8]])
cpd_r = TabularCPD('R', 2, [[0.4], [0.6]])
cpd_j = TabularCPD('J', 2,
                    [[0.9, 0.6, 0.7, 0.1],
                     [0.1, 0.4, 0.3, 0.9]],
                    ['R', 'A'], [2, 2])
cpd_q = TabularCPD('Q', 2,
                    [[0.9, 0.2],
                     [0.1, 0.8]],
                    ['J'], [2])
cpd_l = TabularCPD('L', 2,
                   [[0.9, 0.45, 0.8, 0.1],
                   [0.1, 0.55, 0.2, 0.9]],
                   ['G', 'J'], [2, 2])
cpd_g = TabularCPD('G', 2, [[0.6], [0.4]])

bayesian_model.add_cpds(cpd_a,cpd_r,cpd_j,cpd_q,cpd_l,cpd_g);
belief_propagation = BeliefPropagation(bayesian_model)
print (belief_propagation.map_query(variables=['J', 'Q'], evidence={'A': 0, 'R': 0, 'G': 0, 'L': 1}))