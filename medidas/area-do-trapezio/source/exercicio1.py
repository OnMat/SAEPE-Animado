from manim import *

class cena(Scene):
    def construct(self):
        # TÍTULO
        titulo = Text("Questão – Área do Trapézio (SAEPE - 2022)", font="Fira Sans").scale(0.5)
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


        # Enunciado
        enunciado = Paragraph(
            "Juliana comprou ladrilhos, que possuem o formato de um trapézio, para revestir parte da parede do seu banheiro.",
            "Na figura abaixo está representado um desses ladrilhos com algumas medidas indicadas.",
            alignment="left",
            line_spacing=0.8,
            font="CMU Serif"
        ).scale(0.35)

        enunciado.next_to(grupo_titulo, DOWN, buff=0.3)
        enunciado.align_to(grupo_titulo, LEFT)
        self.play(Write(enunciado, run_time=2))
        self.wait(1)

        # --- DESENHO DO TRAPÉZIO E RÓTULOS --- 
        A = [-3, 0, 0]
        B = [3, 0, 0]
        C = [1.5, 2, 0]
        D = [-1.5, 2, 0]
        trapezio = Polygon(A, B, C, D, color=BLUE, fill_opacity = 0.5)

        base_maior = Line(A, B)
        rotulo_b2 = Tex("20 cm", font_size=24).next_to(base_maior, DOWN, buff=0.2)

        base_menor = Line(D, C)
        rotulo_b1 = Tex("10 cm", font_size=24).next_to(base_menor, UP, buff=0.2)

        ponto_E = [C[0], A[1], 0]
        altura = Line(C, ponto_E, color=YELLOW)
        rotulo_h = Tex("8{,}5 cm", font_size=24).next_to(altura, RIGHT, buff=0.1)

        # Agrupar tudo para mover junto
        trapezio_group = VGroup(trapezio, base_maior, base_menor, altura, rotulo_b1, rotulo_b2, rotulo_h)
        trapezio_group.next_to(enunciado, DOWN, buff=0.4)
        trapezio_group.align_to(enunciado, LEFT)

        self.play(Create(trapezio), Create(base_maior), Write(rotulo_b2),
                  Create(base_menor), Write(rotulo_b1),
                  Create(altura), Write(rotulo_h))
        self.wait(1)

        # --- ALTERNATIVAS ---
        alternativas = VGroup(
            Tex("A) 38,5 cm²", font_size=24),
            Tex("B) 127,5 cm²", font_size=24),
            Tex("C) 170,0 cm²", font_size=24),
            Tex("D) 255,0 cm²", font_size=24),
            Tex("E) 1 700,0 cm²", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT)

        alternativas.next_to(trapezio_group, DOWN, buff=0.2).align_to(enunciado, LEFT)
        self.play(Write(alternativas))
        self.wait(1)

        # --- RESOLUÇÃO DA QUESTÃO ---
        linha1 = MathTex(r"A = \frac{(b_1 + b_2) \cdot h}{2}", font_size=26, color = RED)
        linha2 = MathTex(r"A = \frac{(10 + 20) \cdot 8{,}5}{2}", font_size=26, color = RED)
        linha3 = MathTex(r"A = \frac{30 \cdot 8{,}5}{2}", font_size=26, color = RED)
        linha4 = MathTex(r"A = \frac{255}{2}", font_size=26, color = RED)
        linha5 = MathTex(r"A = 127{,}5", font_size=26, color = RED)
        linha6 = MathTex(r"\therefore\ \boxed{A = 127{,}5\ \text{cm}^2}", font_size=26, color = RED)

        resolucao = VGroup(linha1, linha2, linha3, linha4, linha5, linha6).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        resolucao.move_to(alternativas[0].get_center()).align_to(alternativas, LEFT).shift(RIGHT * 7.2)

        for linha in resolucao:
            self.play(Write(linha))
            self.wait(0.5)

        # --- DESTACAR ALTERNATIVA CORRETA (letra B) ---
        alternativa_correta = alternativas[1]
        self.play(Circumscribe(alternativa_correta, color=YELLOW))
        self.play(Indicate(alternativa_correta, color=YELLOW))
        self.play(alternativa_correta.animate.set_color(YELLOW))
        self.wait(3)