from manim import *

class cena1(Scene):
    def construct(self):
        # TÍTULO
        titulo = Text("Questão – Área do Trapézio (SAEPE - 2016)", font="Fira Sans").scale(0.5)
        self.play(Write(titulo))
        self.wait(0.5)

        linha = Line(
            start=titulo.get_bottom() + DOWN * 0.2 + LEFT * titulo.width / 2,
            end=titulo.get_bottom() + DOWN * 0.2 + RIGHT * titulo.width / 2,
            stroke_width=6
        ).set_color(RED)

        linha.add_updater(lambda m, dt: m.set_color(interpolate_color(RED, BLUE, (np.sin(self.time * 2) + 1) / 2)))
        self.play(FadeIn(linha))
        self.wait(0.5)

        grupo_titulo = VGroup(titulo, linha)
        self.play(grupo_titulo.animate.scale(0.9).to_corner(UL))
        self.wait(1)

        # ENUNCIADO
        enunciado = Paragraph(
            "O trapézio retângulo desenhado abaixo representa uma bancada de mármore",
            "que Andréia colocou em sua cozinha. Qual é a medida da área dessa bancada?",
            alignment="left", line_spacing=0.8, font="CMU Serif"
        ).scale(0.35).next_to(grupo_titulo, DOWN, aligned_edge=LEFT)

        self.play(Write(enunciado, run_time=2))
        self.wait(1)

        # TRAPÉZIO INVERTIDO (menor e com lado inclinado à esquerda)
        A = [-2.5, 0, 0]         # inferior esquerdo
        B = [2.5, 0, 0]          # inferior direito
        C = [2.5, 1.9, 0]        # superior direito
        D = [0.5, 1.9, 0]        # superior esquerdo
        trap = Polygon(A, B, C, D, color=WHITE, fill_color=BLUE, fill_opacity=0.3)

        base_maior = Line(A, B)
        base_menor = Line(D, C)
        altura = Line(D, [D[0], A[1], 0], color=YELLOW)

        rotulo_base_maior = Tex("60 cm", font_size=24).next_to(base_maior, DOWN, buff=0.2)
        rotulo_base_menor = Tex("79 cm", font_size=24).next_to(base_menor, UP, buff=0.2)
        rotulo_altura = Tex("48 cm", font_size=24).next_to(altura, LEFT, buff=0.1)

        trapezio_group = VGroup(trap, base_maior, base_menor, altura,
                                rotulo_base_maior, rotulo_base_menor, rotulo_altura)
        trapezio_group.next_to(enunciado, DOWN, buff=0.5)
        trapezio_group.align_to(enunciado, LEFT)

        self.play(Create(trap))
        self.play(Create(base_maior), Write(rotulo_base_maior))
        self.play(Create(base_menor), Write(rotulo_base_menor))
        self.play(Create(altura), Write(rotulo_altura))
        self.wait(1)

        # ALTERNATIVAS
        alternativas = VGroup(
            Tex("A) 187 cm²", font_size=24),
            Tex("B) 209 cm²", font_size=24),
            Tex("C) 3 336 cm²", font_size=24),
            Tex("D) 6 672 cm²", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT)
        alternativas.next_to(trapezio_group, DOWN, buff=0.8)
        alternativas.align_to(enunciado, LEFT)

        self.play(Write(alternativas))
        self.wait(1)

        # RESOLUÇÃO (à direita)
        linha1 = MathTex(r"A = \frac{(b_1 + b_2) \cdot h}{2}", font_size=26)
        linha2 = MathTex(r"A = \frac{(60 + 79) \cdot 48}{2}", font_size=26)
        linha3 = MathTex(r"A = \frac{139 \cdot 48}{2}", font_size=26)
        linha4 = MathTex(r"A = \frac{6672}{2}", font_size=26)
        linha5 = MathTex(r"A = 3\,336", font_size=26)
        linha6 = MathTex(r"\therefore\ \boxed{A = 3\,336\ \text{cm}^2}", font_size=26, color=YELLOW)

        resolucao = VGroup(linha1, linha2, linha3, linha4, linha5, linha6).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        resolucao.shift(RIGHT * 5.5 + DOWN * 0.5)

        for linha in resolucao:
            self.play(Write(linha))
            self.wait(0.5)

        # DESTAQUE DA ALTERNATIVA CORRETA (letra C)
        alternativa_correta = alternativas[2]
        self.play(Circumscribe(alternativa_correta, color=YELLOW))
        self.play(Indicate(alternativa_correta, color=YELLOW))
        self.play(alternativa_correta.animate.set_color(YELLOW))
        self.wait(3)
