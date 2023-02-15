import compute_entropy as entropy


size1 = int(input())
whole_size = int(input())
entropy1 = float(entropy.calc_entropy())
entropy2 = float(entropy.calc_entropy())
old_entropy = 0.97
inf_gain = old_entropy - ((size1 * entropy1 + (1 - size1) * entropy2) / whole_size)
print("{:.2f}".format(inf_gain))
