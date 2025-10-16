from itertools import product

def implies(a, b):
    return (not a) or b

# Knowledge Base: (Q→P) ∧ (P→¬Q) ∧ (Q∨R)
def KB(P, Q, R):
    return implies(Q, P) and implies(P, not Q) and (Q or R)

# Header
print("P Q R | Q→P P→¬Q Q∨R | KB")
print("-"*36)

models = []

# Truth table generation
for P, Q, R in product([False, True], repeat=3):
    q_imp_p = implies(Q, P)
    p_imp_notq = implies(P, not Q)
    q_or_r = Q or R
    kb_val = q_imp_p and p_imp_notq and q_or_r
    if kb_val:
        models.append((P, Q, R))
    print(f"{int(P)} {int(Q)} {int(R)} |   {int(q_imp_p)}    {int(p_imp_notq)}    {int(q_or_r)}  |  {int(kb_val)}")

# Models where KB is true
print("\nKB True Models:")
for m in models:
    print(f"P={int(m[0])}, Q={int(m[1])}, R={int(m[2])}")

# Entailment checking
def entails(expr):
    return all(expr(P, Q, R) for (P, Q, R) in models)

# Entailment tests
expr_R = lambda P, Q, R: R
expr_R_imp_P = lambda P, Q, R: implies(R, P)
expr_Q_imp_R = lambda P, Q, R: implies(Q, R)

print("\nEntailment Results:")
print("KB ⊨ R        :", entails(expr_R))
print("KB ⊨ (R → P)  :", entails(expr_R_imp_P))
print("KB ⊨ (Q → R)  :", entails(expr_Q_imp_R))

Output:

P Q R | Q→P P→¬Q Q∨R | KB
------------------------------------
0 0 0 |   1    1    0  |  0
0 0 1 |   1    1    1  |  1
0 1 0 |   0    1    1  |  0
0 1 1 |   0    1    1  |  0
1 0 0 |   1    1    0  |  0
1 0 1 |   1    1    1  |  1
1 1 0 |   1    0    1  |  0
1 1 1 |   1    0    1  |  0

KB True Models:
P=0, Q=0, R=1
P=1, Q=0, R=1

Entailment Results:
KB ⊨ R        : True
KB ⊨ (R → P)  : False
KB ⊨ (Q → R)  : True
