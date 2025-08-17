from manim import *

class cena(Scene):
    def construct(self):

        # Título centralizado
        titulo = Text("Questão Progressão Aritmética (SAEPE - 2021)", font="Fira Sans").scale(0.5)
        self.play(Write(titulo))
        self.wait(0.5)

        # Linha exatamente do tamanho do texto
        linha = Line(
            start=titulo.get_bottom() + DOWN * 0.2 + LEFT * titulo.width / 2,
            end=titulo.get_bottom() + DOWN * 0.2 + RIGHT * titulo.width / 2,
            stroke_width=6
        ).set_color(RED)

        # Atualizador de cor animada
        linha.add_updater(lambda m, dt: m.set_color(interpolate_color(RED, BLUE, (np.sin(self.time * 2) + 1) / 2)))
        self.play(FadeIn(linha))
        self.wait(0.5)

        # Agrupamento e movimento animado para o canto superior esquerdo
        grupo_titulo = VGroup(titulo, linha)
        self.play(grupo_titulo.animate.scale(0.9).to_corner(UL))
        self.wait(1)

        # Enunciado
        enunciado = Paragraph(
            r"Dentre os anos de 2000 e 2012, a exportação de uma fruta aumentou 5 000 toneladas a cada ano. Em 2010, a exportação foi",
            r"de 103 000 toneladas. Quantas toneladas foram exportadas no ano 2000?",
            alignment="left",
            line_spacing=0.8, 
            font="CMU Serif"
        ).scale(0.35).next_to(grupo_titulo, DOWN, aligned_edge=LEFT)

        self.play(Write(enunciado, run_time=2))
        self.wait(0.5)

        # Fórmula
        formula = MathTex(r"a_n = a_1 + (n - 1) \cdot r").scale(0.65)
        formula.next_to(enunciado, DOWN, buff=0.8).align_to(enunciado, LEFT)
        self.play(Write(formula))
        self.wait(0.5)

        # Alternativas
        alternativas = VGroup(
            Tex("A) 58 000", font_size=24),
            Tex("B) 53 000", font_size=24),
            Tex("C) 9 800", font_size=24),
            Tex("D) 7 923", font_size=24),
            Tex("E) 5 300", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        alternativas.next_to(formula, DOWN, buff=0.8).align_to(formula, LEFT)
        self.play(Write(alternativas))
        self.wait(1)

        

        # Resolução passo a passo
        passo1 = MathTex(r"a_{11} = 103\,000", font_size=26)
        passo2 = MathTex(r"a_1 + 10 \cdot 5\,000 = 103\,000", font_size=26)
        passo3 = MathTex(r"a_1 + 50\,000 = 103\,000", font_size=26)
        passo4 = MathTex(r"a_1 = 103\,000 - 50\,000", font_size=26)
        passo5 = MathTex(r"a_1 = 53\,000", font_size=26, color=YELLOW)

        passos = VGroup(passo1, passo2, passo3, passo4, passo5).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        passos.shift(RIGHT * 2.8 + DOWN * 1)

        for p in passos:
            self.play(Write(p))
            self.wait(0.4)


        # Destacar alternativa correta (letra B)
        alternativa_correta = alternativas[1]
        self.play(Circumscribe(alternativa_correta, color=YELLOW))
        self.play(Indicate(alternativa_correta, color=YELLOW))
        self.play(alternativa_correta.animate.set_color(YELLOW))
        self.wait(2)
