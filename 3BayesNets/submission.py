import sys

"""
WRITE YOUR CODE BELOW.
"""
from numpy import zeros, float32

#  pgmpy͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
import pgmpy
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import random

# You are not allowed to use following set of modules from 'pgmpy' Library.͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
#
# pgmpy.sampling.*͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
# pgmpy.factors.*͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
# pgmpy.estimators.*͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉


def make_security_system_net():
    """Create a Bayes Net representation of the above security system problem.
    Use the following as the name attribute: "H","C", "M","B", "Q", 'K",
    "D"'. (for the tests to work.)
    """
    BayesNet = BayesianNetwork()
    # TODO: finish this function͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
    BayesNet.add_node("H")
    BayesNet.add_node("C")
    BayesNet.add_node("M")
    BayesNet.add_node("B")
    BayesNet.add_node("Q")
    BayesNet.add_node("K")
    BayesNet.add_node("D")
    BayesNet.add_edge("H", "Q")
    BayesNet.add_edge("C", "Q")
    BayesNet.add_edge("M", "K")
    BayesNet.add_edge("B", "K")
    BayesNet.add_edge("Q", "D")
    BayesNet.add_edge("K", "D")
    return BayesNet


def set_probability(bayes_net):
    """Set probability distribution for each node in the security system.
    Use the following as the name attribute: "H","C", "M","B", "Q", 'K",
    "D"'. (for the tests to work.)
    """
    # TODO: set the probability distribution for each node͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
    cpd_H = TabularCPD("H", 2, values=[[0.5], [0.5]])
    cpd_C = TabularCPD("C", 2, values=[[0.7], [0.3]])
    cpd_M = TabularCPD("M", 2, values=[[0.2], [0.8]])
    cpd_B = TabularCPD("B", 2, values=[[0.5], [0.5]])
    cpd_Q = TabularCPD(
        "Q",
        2,
        values=[[0.95, 0.75, 0.45, 0.1], [0.05, 0.25, 0.55, 0.9]],
        evidence=["H", "C"],
        evidence_card=[2, 2],
    )
    cpd_K = TabularCPD(
        "K",
        2,
        values=[[0.25, 0.99, 0.05, 0.85], [0.75, 0.01, 0.95, 0.15]],
        evidence=["M", "B"],
        evidence_card=[2, 2],
    )
    cpd_D = TabularCPD(
        "D",
        2,
        values=[[0.98, 0.65, 0.4, 0.01], [0.02, 0.35, 0.6, 0.99]],
        evidence=["Q", "K"],
        evidence_card=[2, 2],
    )
    bayes_net.add_cpds(cpd_H, cpd_C, cpd_M, cpd_B, cpd_Q, cpd_K, cpd_D)
    return bayes_net


def get_marginal_double0(bayes_net):
    """Calculate the marginal probability that Double-0 gets compromised."""
    # TODO: finish this function͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
    solver = VariableElimination(bayes_net)
    marginal_prob = solver.query(variables=["D"], joint=False)
    double0_prob = marginal_prob["D"].values[1]
    return double0_prob


def get_conditional_double0_given_no_contra(bayes_net):
    """Calculate the conditional probability that Double-0 gets compromised
    given Contra is shut down.
    """
    # TODO: finish this function͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
    solver = VariableElimination(bayes_net)
    conditional_prob = solver.query(variables=["D"], evidence={"C": 0}, joint=False)
    double0_prob = conditional_prob["D"].values[1]
    return double0_prob


def get_conditional_double0_given_no_contra_and_bond_guarding(bayes_net):
    """Calculate the conditional probability that Double-0 gets compromised
    given Contra is shut down and Bond is reassigned to protect M.
    """
    # TODO: finish this function͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
    solver = VariableElimination(bayes_net)
    conditional_prob = solver.query(
        variables=["D"], evidence={"C": 0, "B": 1}, joint=False
    )
    double0_prob = conditional_prob["D"].values[1]
    return double0_prob


def get_game_network():
    """Create a Bayes Net representation of the game problem.
    Name the nodes as "A","B","C","AvB","BvC" and "CvA"."""
    BayesNet = BayesianNetwork()
    # TODO: fill this out͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
    BayesNet.add_node("A")
    BayesNet.add_node("B")
    BayesNet.add_node("C")
    BayesNet.add_node("AvB")
    BayesNet.add_node("BvC")
    BayesNet.add_node("CvA")
    BayesNet.add_edge("A", "AvB")
    BayesNet.add_edge("A", "CvA")
    BayesNet.add_edge("B", "AvB")
    BayesNet.add_edge("B", "BvC")
    BayesNet.add_edge("C", "BvC")
    BayesNet.add_edge("C", "CvA")

    cpd_A = TabularCPD("A", 4, values=[[0.15], [0.45], [0.3], [0.1]])
    cpd_B = TabularCPD("B", 4, values=[[0.15], [0.45], [0.3], [0.1]])
    cpd_C = TabularCPD("C", 4, values=[[0.15], [0.45], [0.3], [0.1]])

    skill_diff = {
        0: [0.1, 0.1, 0.8],
        1: [0.2, 0.6, 0.2],
        2: [0.15, 0.75, 0.1],
        3: [0.05, 0.9, 0.05],
        -1: [0.6, 0.2, 0.2],
        -2: [0.75, 0.15, 0.1],
        -3: [0.9, 0.05, 0.05],
    }

    table_avb = zeros((16, 3), dtype=float32)
    for i in range(4):
        for j in range(4):
            table_avb[i * 4 + j] = skill_diff[j - i]

    list_0 = [table_avb[i][0] for i in range(16)]
    list_1 = [table_avb[i][1] for i in range(16)]
    list_2 = [table_avb[i][2] for i in range(16)]
    values = [list_0, list_1, list_2]
    # print(values[0])
    # print(values[1])
    # print(values[2])
    cpd_AvB = TabularCPD("AvB", 3, values, evidence=["A", "B"], evidence_card=[4, 4])
    cpd_BvC = TabularCPD("BvC", 3, values, evidence=["B", "C"], evidence_card=[4, 4])
    cpd_CvA = TabularCPD("CvA", 3, values, evidence=["C", "A"], evidence_card=[4, 4])
    BayesNet.add_cpds(cpd_A, cpd_B, cpd_C, cpd_AvB, cpd_BvC, cpd_CvA)

    return BayesNet


def calculate_posterior(bayes_net):
    """Calculate the posterior distribution of the BvC match given that A won against B and tied C.
    Return a list of probabilities corresponding to win, loss and tie likelihood."""
    posterior = [0, 0, 0]
    # TODO: finish this function͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
    solver = VariableElimination(bayes_net)
    posterior = solver.query(
        variables=["BvC"], evidence={"AvB": 0, "CvA": 2}, joint=False
    )
    posterior = posterior["BvC"].values
    # print(posterior[0], posterior[1], posterior[2])
    return posterior  # list


def Gibbs_sampler(bayes_net, initial_state):
    """Complete a single iteration of the Gibbs sampling algorithm
    given a Bayesian network and an initial state value.

    initial_state is a list of length 6 where:
    index 0-2: represent skills of teams A,B,C (values lie in [0,3] inclusive)
    index 3-5: represent results of matches AvB, BvC, CvA (values lie in [0,2] inclusive)

    Returns the new state sampled from the probability distribution as a tuple of length 6.
    Return the sample as a tuple.
    """

    # TODO: finish this function͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
    if initial_state is None or len(initial_state) != 6:
        initial_state = []
        for _ in range(3):
            initial_state.append(random.choice(range(4)))
        # AvB is 0, CvA is 2
        initial_state.append(0)
        initial_state.append(random.choice(range(3)))
        initial_state.append(2)
        sample = tuple(initial_state)
    else:
        sample = tuple(initial_state)
    # print(sample, "before change sample")
    variable_update = random.choice([0, 1, 2, 4])
    # print(variable_update, "variable_update")

    # A, B, C are same, use A_cpd represent, AvB, BvC, CvA are same, use AvB_cpd represent
    A_cpd = bayes_net.get_cpds("A")
    # team_table = [0.15, 0.45, 0.3, 0.1]
    team_table = A_cpd.values
    AvB_cpd = bayes_net.get_cpds("AvB")
    #     match_table = [
    #                    [[0.1      0.2       0.15       0.05]
    #                     [0.6      0.1       0.2        0.15]
    #                     [0.75     0.6       0.1        0.2 ]
    #                     [0.90     0.75      0.6        0.1 ]]
    #                    [[0.1      0.6       0.75       0.90]
    #                     [0.2      0.1       0.6        0.75]
    #                     [0.15     0.2       0.1        0.6 ]
    #                     [0.05     0.15      0.2        0.1 ]]
    #                    [[0.80     0.2       0.1        0.05]
    #                     [0.2      0.80      0.2        0.1 ]
    #                     [0.1      0.2       0.80       0.2 ]
    #                     [0.05     0.1       0.2        0.80]]
    #                    ]
    match_table = AvB_cpd.values

    # A node update, full conditional prob distribution is
    # P(A) x P(B) x P(C) x P(AvB=0|A, B) x P(AvC=0|A, C) x P(BvC=0|B, C) from ed disscussion #793,
    # more efficitently by considering only its Markov blanket.
    if variable_update == 0:
        sample = list(sample)
        joint_prob = zeros(4, dtype=float32)
        for i in range(4):
            joint_prob[i] = (
                team_table[i]
                * team_table[sample[1]]
                * team_table[sample[2]]
                * match_table[0][i][sample[1]]
                * match_table[2][sample[2]][i]
            )
        joint_prob = joint_prob / sum(joint_prob)
        # weights: A sequence of weights, must be the same length as the population sequence.
        sample = random.choices(range(4), weights=joint_prob) + sample[1:]
        sample = tuple(sample)

    elif variable_update == 1:
        sample = list(sample)
        joint_prob = zeros(4, dtype=float32)
        for i in range(4):
            joint_prob[i] = (
                team_table[sample[0]]
                * team_table[i]
                * team_table[sample[2]]
                * match_table[0][sample[0]][i]
                * match_table[sample[4]][i][sample[2]]
            )
        joint_prob = joint_prob / sum(joint_prob)
        sample = sample[:1] + random.choices(range(4), weights=joint_prob) + sample[2:]
        sample = tuple(sample)

    elif variable_update == 2:
        sample = list(sample)
        joint_prob = zeros(4, dtype=float32)
        for i in range(4):
            joint_prob[i] = (
                team_table[sample[0]]
                * team_table[sample[1]]
                * team_table[i]
                * match_table[sample[4]][sample[1]][i]
                * match_table[2][i][sample[0]]
            )
        joint_prob = joint_prob / sum(joint_prob)
        sample = sample[:2] + random.choices(range(4), weights=joint_prob) + sample[3:]
        sample = tuple(sample)

    else:
        sample = list(sample)
        joint_prob = zeros(3, dtype=float32)
        for i in range(3):
            joint_prob[i] = (
                match_table[i][sample[1]][sample[2]]
                * team_table[sample[1]]
                * team_table[sample[2]]
            )
        joint_prob = joint_prob / sum(joint_prob)
        sample = sample[:4] + random.choices(range(3), weights=joint_prob) + sample[5:]
        sample = tuple(sample)
    return sample


def MH_sampler(bayes_net, initial_state):
    """Complete a single iteration of the MH sampling algorithm given a Bayesian network and an initial state value.
    initial_state is a list of length 6 where:
    index 0-2: represent skills of teams A,B,C (values lie in [0,3] inclusive)
    index 3-5: represent results of matches AvB, BvC, CvA (values lie in [0,2] inclusive)
    Returns the new state sampled from the probability distribution as a tuple of length 6.
    """
    A_cpd = bayes_net.get_cpds("A")
    AvB_cpd = bayes_net.get_cpds("AvB")
    match_table = AvB_cpd.values
    team_table = A_cpd.values

    # TODO: finish this function͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
    if initial_state is None or len(initial_state) != 6:
        initial_state = []
        for _ in range(3):
            initial_state.append(random.choice(range(4)))
        # AvB is 0, CvA is 2
        initial_state.append(0)
        initial_state.append(random.choice(range(3)))
        initial_state.append(2)
        sample = tuple(initial_state)
    else:
        sample = tuple(initial_state)

    current_state = list(sample)
    current_prob = (
        team_table[current_state[0]]
        * team_table[current_state[1]]
        * team_table[current_state[2]]
        * match_table[current_state[3]][current_state[0]][current_state[1]]
        * match_table[current_state[4]][current_state[1]][current_state[2]]
        * match_table[current_state[5]][current_state[2]][current_state[0]]
    )
    # print(current_prob, "current_prob")
    candidate_state = []
    for _ in range(3):
        candidate_state.append(random.choice(range(4)))
    candidate_state.append(0)
    candidate_state.append(random.choice(range(3)))
    candidate_state.append(2)
    candidate_prob = (
        team_table[candidate_state[0]]
        * team_table[candidate_state[1]]
        * team_table[candidate_state[2]]
        * match_table[candidate_state[3]][candidate_state[0]][candidate_state[1]]
        * match_table[candidate_state[4]][candidate_state[1]][candidate_state[2]]
        * match_table[candidate_state[5]][candidate_state[2]][candidate_state[0]]
    )
    candidate_state = tuple(candidate_state)
    # print(candidate_prob, "candidate_prob")
    acceptance_ratio = candidate_prob / current_prob
    # print(acceptance_ratio, "acceptance_ratio")
    if candidate_prob > current_prob:
        sample = candidate_state
    else:
        if random.random() < acceptance_ratio:
            sample = candidate_state
    return sample


def compare_sampling(bayes_net, initial_state):
    """Compare Gibbs and Metropolis-Hastings sampling by calculating how long it takes for each method to converge."""
    Gibbs_count = 0
    MH_count = 0
    MH_rejection_count = 0
    Gibbs_convergence = [
        0,
        0,
        0,
    ]  # posterior distribution of the BvC match as produced by Gibbs
    MH_convergence = [
        0,
        0,
        0,
    ]  # posterior distribution of the BvC match as produced by MH
    # TODO: finish this function͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
    count = 500000
    burn = 20000
    delta = 0.01
    N = 20
    sample_gibbs = initial_state
    sample_MH = initial_state
    gibbs_BvC = [0, 0, 0]
    MH_BvC = [0, 0, 0]
    for _ in range(count):
        Gibbs_count += 1
        sample_gibbs = Gibbs_sampler(bayes_net, sample_gibbs)
        gibbs_BvC[sample_gibbs[4]] += 1
        if _ > burn:
            old_gibbs = Gibbs_convergence
            Gibbs_convergence = [
                gibbs_BvC[0] / (Gibbs_count),
                gibbs_BvC[1] / (Gibbs_count),
                gibbs_BvC[2] / (Gibbs_count),
            ]
            if (
                abs(Gibbs_convergence[0] - old_gibbs[0]) < delta
                and abs(Gibbs_convergence[0] - old_gibbs[0]) != 0
                and abs(Gibbs_convergence[1] - old_gibbs[1]) < delta
                and abs(Gibbs_convergence[1] - old_gibbs[1]) != 0
                and abs(Gibbs_convergence[2] - old_gibbs[2]) < delta
                and abs(Gibbs_convergence[2] - old_gibbs[2]) != 0
            ):
                N -= 1
                if N == 0:
                    # if (
                    #     abs(Gibbs_convergence[0] - 0.25) < 0.01
                    #     and abs(Gibbs_convergence[1] - 0.42) < 0.01
                    #     and abs(Gibbs_convergence[2] - 0.31) < 0.01
                    # ):
                    break
            else:
                N = 20
    N = 20
    for _ in range(count):
        MH_count += 1
        old_MH = sample_MH
        sample_MH = MH_sampler(bayes_net, sample_MH)
        if sample_MH == old_MH:
            MH_rejection_count += 1
        MH_BvC[sample_MH[4]] += 1
        if _ > burn:
            old_MH = MH_convergence
            MH_convergence = [
                MH_BvC[0] / (MH_count),
                MH_BvC[1] / (MH_count),
                MH_BvC[2] / (MH_count),
            ]
            if (
                abs(MH_convergence[0] - old_MH[0]) < delta
                and abs(MH_convergence[0] - old_MH[0]) != 0
                and abs(MH_convergence[1] - old_MH[1]) < delta
                and abs(MH_convergence[1] - old_MH[1]) != 0
                and abs(MH_convergence[2] - old_MH[2]) < delta
                and abs(MH_convergence[2] - old_MH[2]) != 0
            ):
                N -= 1
                if N == 0:
                    # if (
                    #     abs(MH_convergence[0] - 0.25) < 0.01
                    #     and abs(MH_convergence[1] - 0.42) < 0.01
                    #     and abs(MH_convergence[2] - 0.31) < 0.01
                    # ):
                    break
            else:
                N = 20
    return Gibbs_convergence, MH_convergence, Gibbs_count, MH_count, MH_rejection_count


def sampling_question():
    """Question about sampling performance."""
    # TODO: assign value to choice and factor͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
    # through compare_sampling results, it decided by initial_state
    choice = 1
    options = ["Gibbs", "Metropolis-Hastings"]
    factor = 1
    return options[choice], factor


def return_your_name():
    """Return your name from this function"""
    # TODO: finish this function͏󠄂͏️͏󠄌͏󠄎͏︀͏︄͏󠄉
    return "Jing Li"
