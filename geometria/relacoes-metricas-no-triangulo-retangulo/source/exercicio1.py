from manim import *

class cena(Scene):
    def construct(self):

# Título com linha animada
        t5 = Text("Questão Relações métricas (SAEPE - 2022)", font="Fira Sans").scale(0.5)
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

        # Texto explicativo
        explicacao5 = Paragraph(
            "Uma estrutura metálica em formato de triângulo retângulo será reforçada com a soldagem de uma nova barra de metal.",
            "Essa barra será fixada na posição do segmento que representa a altura h, relativa à hipotenusa desse triângulo,",
            "conforme ilustrado na figura abaixo.",
            alignment="left",
            line_spacing=0.8,
            font="CMU Serif"
        ).scale(0.35)
        explicacao5.next_to(grupo_titulo5, DOWN, buff=0.3).align_to(grupo_titulo5, LEFT)
        self.play(Write(explicacao5, run_time=1))
        self.wait(0.5)


        # Pontos do triângulo
        A5 = np.array([-2, -1, 0])
        B5 = np.array([2, -1, 0])
        C5 = np.array([2, 1.5, 0])
        D5 = np.array([0.876, 0.798, 0])

        # Triângulo ABC
        triangulo5 = Polygon(A5, B5, C5, stroke_width=3)

        segmento5 = Line(B5, D5, stroke_width=4)

        # Primeiro quadrado - centro em [2, -1, 0]
        centro1 = np.array([1.85, -0.9, 0])
        quadrado1 = Square(side_length=0.25).move_to(centro1)
        ponto1 = Dot(centro1, color=RED).scale(0.5)

        # Segundo quadrado - centro em [0.9, 0.8, 0], rotacionado 50 graus
        centro2 = np.array([1.05, 0.75, 0])
        quadrado2 = Square(side_length=0.25).move_to(centro2)
        quadrado2.rotate(34 * DEGREES)  # 50 graus em radianos
        ponto2 = Dot(centro2, color=RED).scale(0.5)

        # Adiciona tudo na cena
        self.add(quadrado1, ponto1, quadrado2, ponto2)
        self.play(Create(segmento5), Create(quadrado1), Create(ponto1), Create(quadrado2), Create(ponto2), Create(triangulo5))
        self.wait(1)

        # Segmentos CD e DA (não adicionados à cena, apenas usados para os rótulos)
        segmento_CD5 = Line(C5, D5)
        segmento_DA5 = Line(D5, A5)

        # Rótulos dos segmentos
        rotulo_CD5 = Tex("0{,}4 m", font_size=24).next_to(segmento_CD5.get_center(), UP, buff=0.1).rotate(34 * DEGREES)
        rotulo_DA5 = Tex("0{,}9 m", font_size=24).next_to(segmento_DA5.get_center(), UP, buff=0.1).rotate(34 * DEGREES)

        # Adiciona apenas os rótulos à cena
        self.play(Write(rotulo_CD5), Write(rotulo_DA5))

                

        # Alternativas alinhadas com o texto, abaixo do triângulo
        alternativas = VGroup(
            Tex("A) 0{,}28 m", font_size=24),
            Tex("B) 0{,}36 m", font_size=24),
            Tex("C) 0{,}40 m", font_size=24),
            Tex("D) 0{,}50 m", font_size=24),
            Tex("E) 0{,}60 m", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT)

        alternativas.next_to(triangulo5, DOWN, buff=0.1).align_to(explicacao5, LEFT)
        self.play(Write(alternativas))
        self.wait(1)

        # Resolução da questão — linha por linha
        linha15 = MathTex(r"m = 0.4", font_size=28, color=RED)
        linha25 = MathTex(r"n = 0.9", font_size=28, color=RED)
        linha35 = MathTex(r"h^2 = m \cdot n = 0.4 \cdot 0.9 = 0.36", font_size=28, color=RED)
        linha45 = MathTex(r"h = \sqrt{0.36} = 0.6\ \text{m}", font_size=28, color=RED)

        # Agrupamento e posicionamento
        resolucao = VGroup(linha15, linha25, linha35, linha45).arrange(DOWN, aligned_edge=LEFT)
        resolucao.next_to(triangulo5, DOWN, buff=1)

        # Animações uma a uma
        self.play(Write(linha15))
        self.wait(0.8)

        self.play(Write(linha25))
        self.wait(0.8)

        self.play(Write(linha35))
        self.wait(1)

        self.play(Write(linha45))
        self.wait(2)

                # DESTACAR ALTERNATIVA CORRETA (E)
        alternativa_correta = alternativas[4]

        # 1. Circunda a alternativa
        self.play(Circumscribe(alternativa_correta, color=YELLOW))
        # 2. Destaca com brilho
        self.play(Indicate(alternativa_correta, color=YELLOW))
        # 3. Altera cor fixa
        self.play(alternativa_correta.animate.set_color(YELLOW))
        self.wait(4)