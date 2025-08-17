from manim import *
from pathlib import Path
import os

class cena1(Scene):
    def construct(self):


# --- Título com linha animada ---
        t5 = Text("Questão Progressão Aritmética (SAEPE - 2019)", font="Fira Sans").scale(0.5)
        self.play(Write(t5, run_time=2))
        self.wait(0.5)

        linha5 = Line(
            start=t5.get_bottom() + DOWN * 0.2 + LEFT * t5.width / 2,
            end=t5.get_bottom() + DOWN * 0.2 + RIGHT * t5.width / 2,
            stroke_width=6,
        )
        linha5.set_color(RED)

        def atualizar_linha5(obj, dt):
            tempo = self.time
            nova_cor = interpolate_color(RED, BLUE, (np.sin(tempo * 2) + 1) / 2)
            obj.set_color(nova_cor)

        linha5.add_updater(atualizar_linha5)
        self.play(FadeIn(linha5))
        self.wait(1)

        grupo_titulo5 = VGroup(t5, linha5)
        self.play(grupo_titulo5.animate.scale(0.9).to_corner(UL), run_time=1.5)
        self.wait(1)

        # --- Enunciado ---
        enunciado = Paragraph(
            "Em março de 2017, Taís começou a trabalhar como manicure e comprou 8 vidros de esmalte. Após isso, a cada mês, ela comprou",
            "2 vidros de esmalte a mais do que havia comprado no mês anterior. Em agosto de 2017, o preço de cada vidro de esmalte",
            "era R$ 3,75. A quantia gasta por Taís, em agosto de 2017, na compra desses vidros de esmalte foi:",
            alignment="left",
            line_spacing=0.8,
            font="CMU Serif"
        ).scale(0.35)

        enunciado.next_to(grupo_titulo5, DOWN, buff=0.3)
        enunciado.align_to(grupo_titulo5, LEFT)
        self.play(Write(enunciado, run_time=2))
        self.wait(1)

        formula_geral1 = MathTex(r'a_n = a_1 + (n - 1) \cdot r').scale(0.7)
        formula_geral1.next_to(enunciado, DOWN, buff=0.3)
        formula_geral1.align_to(enunciado, LEFT)
        self.play(Write(formula_geral1))
        self.wait(1)

        # --- Alternativas ---
        alternativas = VGroup(
            Tex("A) R\$ 37{,}50", font_size=24),
            Tex("B) R\$ 45{,}00", font_size=24),
            Tex("C) R\$ 52{,}50", font_size=24),
            Tex("D) R\$ 67{,}50", font_size=24),
            Tex("E) R\$ 75{,}00", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT)

        alternativas.next_to(enunciado, DOWN, buff=1.6).align_to(enunciado, LEFT)
        self.play(Write(alternativas))
        self.wait(1)

        # --- Resolução PARTE 1 ---
        parte1 = VGroup(
            MathTex(r"a_1 = 8", font_size=26),
            MathTex(r"r = 2", font_size=26),
            MathTex(r"n = 6", font_size=26, color=BLUE),
            MathTex(r"a_6 = 8 + (6 - 1) \cdot 2", font_size=26),
            MathTex(r"a_6 = 8 + 10 = 18", font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        parte1.next_to(alternativas, RIGHT, buff=1)
        parte1.align_to(alternativas, UP)
        for linha in parte1:
            self.play(Write(linha))
            self.wait(0.5)

        # --- Resolução PARTE 2 ---
        parte2 = VGroup(
            MathTex(r"\text{Custo} = 18 \cdot 3{,}75", font_size=26),
            MathTex(r"\text{Custo} = 67{,}50", font_size=26),
            MathTex(r"\therefore\ \boxed{\text{R\$ 67{,}50}}", font_size=26, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        parte2.next_to(parte1, RIGHT, buff=1)
        parte2.align_to(parte1, UP)
        for linha in parte2:
            self.play(Write(linha))
            self.wait(0.5)

        # --- Destacar alternativa correta (letra D) ---
        alternativa_correta = alternativas[3]
        self.play(Circumscribe(alternativa_correta, color=YELLOW))
        self.play(Indicate(alternativa_correta, color=YELLOW))
        self.play(alternativa_correta.animate.set_color(YELLOW))
        self.wait(3)


