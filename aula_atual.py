# lista = [
#  numero * 2
#  for numero in range(10)
# ]
# print(lista)


from dataclasses import dataclass
from typing import List, Optional, Tuple, Union

# Representação de fórmulas:
# - átomo: "P", "Q", "R"
# - implicação: ("imp", antecedente, consequente)

Formula = Union[str, Tuple[str, "Formula", "Formula"]]


@dataclass
class ProofStep:
    number: int
    formula: Formula
    justification: str


def formula_to_str(f: Formula) -> str:
    if isinstance(f, str):
        return f
    if isinstance(f, tuple) and f[0] == "imp":
        left = formula_to_str(f[1])
        right = formula_to_str(f[2])
        return f"({left} -> {right})"
    return str(f)


def is_implication(f: Formula) -> bool:
    return isinstance(f, tuple) and len(f) == 3 and f[0] == "imp"


def modus_ponens(steps: List[ProofStep]) -> Optional[ProofStep]:
    """
    Procura por duas linhas:
      i) A
     ii) A -> B
    e produz B.
    """
    known_formulas = {step.formula: step.number for step in steps}

    for step in steps:
        if is_implication(step.formula):
            antecedent = step.formula[1]
            consequent = step.formula[2]

            if antecedent in known_formulas and consequent not in known_formulas:
                ant_line = known_formulas[antecedent]
                imp_line = step.number
                return ProofStep(
                    number=len(steps) + 1,
                    formula=consequent,
                    justification=f"->E em {ant_line}, {imp_line}"
                )
    return None


def prove(goal: Formula, premises: List[Formula]) -> List[ProofStep]:
    """
    Constrói uma prova simples por encadeamento de Modus Ponens.
    """
    steps = [
        ProofStep(i + 1, premise, "Premissa")
        for i, premise in enumerate(premises)
    ]

    while True:
        # Verifica se o objetivo já foi provado
        if any(step.formula == goal for step in steps):
            return steps

        new_step = modus_ponens(steps)

        if new_step is None:
            raise ValueError(
                f"Não foi possível deduzir {formula_to_str(goal)} com as regras implementadas."
            )

        steps.append(new_step)


def print_proof(steps: List[ProofStep]) -> None:
    print("Prova em Dedução Natural:\n")
    for step in steps:
        print(f"{step.number:>2}. {formula_to_str(step.formula):<12} {step.justification}")


if __name__ == "__main__":
    # Premissas:
    # 1. P -> Q
    # 2. Q -> R
    # 3. P
    premises = [
        ("imp", "P", "Q"),
        ("imp", "Q", "R"),
        "P"
    ]

    goal = "R"

    proof = prove(goal, premises)
    print_proof(proof)