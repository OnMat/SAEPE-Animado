from manim import *

class cena(Scene):
    def construct(self):
    
       
        # ABERTURA DO VÍDEO
        inicio = Text("SAEPE Animado")
        fim = inicio.copy()
        triangulo = Triangle(color=BLUE)
        retangulo = Rectangle(width=2.5, height=1.5, color=GREEN)
        pentagono = RegularPolygon(n=5, radius=1, color=ORANGE)
        hexagono = RegularPolygon(n=6, radius=1, color=PURPLE)
        
        self.wait()
        self.play(Write(inicio))
        self.wait()
        self.play(Transform(
            inicio,
            fim.shift(2*UP),
            path_func=utils.paths.straight_path(),
            run_time=1.5,
        ))
        self.wait()

        triangulo.shift(LEFT * 4.5)
        retangulo.shift(LEFT * 1.6)
        pentagono.shift(RIGHT * 1.6)
        hexagono.shift(RIGHT * 4.5)

        self.play(Create(triangulo), Create(retangulo),
                  Create(pentagono), Create(hexagono))
        self.wait(1)

        # AGRUPAMENTO E REDUÇÃO DAS FIGURAS
        grupo1 = VGroup(triangulo, retangulo, pentagono, hexagono)
        self.play(grupo1.animate.scale(0.7))
        self.wait(0.5)

        for _ in range(4):
            self.play(CyclicReplace(*grupo1))
        self.wait(1)

        # Agora adiciona o texto e agrupa tudo
        titulo_gp = Text(
            "Geometria", font="Fira Sans").scale(0.75)
        titulo_gp.next_to(grupo1, DOWN, buff=0.8)

        self.play(Write(titulo_gp))
        self.wait(1)

        grupo_com_texto = VGroup(grupo1, titulo_gp, inicio)
        self.play(FadeOut(grupo_com_texto))
        t1 = Text("Relações Métricas no Triângulo Retângulo", font="Fira Sans").scale(0.5)
        self.play(Write(t1, run_time=2))
        self.wait(0.5)

        linha = Line(
            start=t1.get_bottom() + DOWN * 0.2 + LEFT * t1.width / 2,
            end=t1.get_bottom() + DOWN * 0.2 + RIGHT * t1.width / 2,
            stroke_width=6,
        )
        linha.set_color(RED)

        # Função para atualizar a cor da linha
        def atualizar_linha(obj, dt):
            t = self.time
            nova_cor = interpolate_color(RED, BLUE, (np.sin(t * 2) + 1) / 2)
            obj.set_color(nova_cor)

        linha.add_updater(atualizar_linha)
        self.play(FadeIn(linha))
        self.wait(1)


        grupo_titulo = VGroup(t1, linha)
        self.play(grupo_titulo.animate.scale(0.9).to_corner(UL))
        self.wait(1)


        explicacao = Paragraph(
            r"   As relações métricas no triângulo retângulo são expressões matemáticas que relacionam as medidas de alguns elementos do",
            r"triângulo retângulo. Dentre esses elementos, destacam-se a hipotenusa, os catetos, a altura relativa à hipotenusa à e as ",
            r"projeções dos catetos sobre a hipotenusa. Para o estudo dessas relações, consideraremos a situação a seguir.",
            r"",
            r"",
            r"Dado o triângulo ABC, retângulo em A, temos:",
            alignment="left",
            line_spacing=0.8, font="CMU Serif"
        ).scale(0.35)

        # Posiciona abaixo e alinha à esquerda com o grupo
        explicacao.next_to(grupo_titulo, DOWN, buff=0.3)
        explicacao.align_to(grupo_titulo, LEFT)  # <- ESSENCIAL!

        self.play(Write(explicacao, run_time = 1))
        self.wait(1)


        # Deslocamento para esquerda e para baixo
        deslocamento = np.array([-2.8, -2, 0])

        # Vértices do triângulo (ângulo reto em A)
        A = np.array([0, 2, 0]) + deslocamento
        B = np.array([-1, 0.27, 0]) + deslocamento
        C = np.array([3.03, 0.25, 0]) + deslocamento
        D = np.array([0, 0.263, 0]) + deslocamento  # já deslocado junto

        triangulo = Polygon(B, A, C, color=WHITE)
        self.play(Create(triangulo))

        ponto_A = Dot(A)
        ponto_B = Dot(B)
        ponto_C = Dot(C)

        label_A = Tex("A").scale(0.6).next_to(ponto_A, UP, buff=0.1)
        label_B = Tex("B").scale(0.6).next_to(ponto_B, DOWN + LEFT, buff=0.1)
        label_C = Tex("C").scale(0.6).next_to(ponto_C, DOWN + RIGHT, buff=0.1)

        self.play(FadeIn(ponto_A), FadeIn(ponto_B), FadeIn(ponto_C))
        self.play(Write(label_A), Write(label_B), Write(label_C))

        # Brace embaixo de BC, já na posição final e mais fino
        brace_a_baixo = Brace(Line(B, C), direction=DOWN, color=WHITE, stroke_width=0.5)
        label_a_baixo = brace_a_baixo.get_text("a").scale(0.7)

        # Lados b e c
        lado_b = Tex("b").scale(0.7).move_to((A + C) / 2 + UP * 0.25)
        lado_c = Tex("c").scale(0.7).move_to((A + B) / 2 + LEFT * 0.25)

        self.play(Write(lado_b), Write(lado_c))
        self.play(Create(brace_a_baixo), Write(label_a_baixo))
        self.wait(1)


        # Altura em vermelho (agora usando o D já deslocado)
        altura = DashedLine(A, D, color=RED)
        ponto_D = Dot(D, color=RED).set_z_index(2)
        label_D = Tex("D").scale(0.5).next_to(ponto_D, UP + RIGHT, buff=0.1)
        label_altura = Tex("h").scale(0.7).next_to(altura, RIGHT, buff=0.1)

        

        self.play(Create(altura))
        self.play(FadeIn(ponto_D))
        self.play(FadeIn(label_D))
        self.play(Write(label_altura))
        self.wait(1)

        # Projeções m e n com cores distintas
        linha_m = Line(B, D, color=PURPLE)
        linha_n = Line(D, C, color=YELLOW)

        label_m = Tex("m").scale(0.7).next_to(linha_m, UP, buff=0.1)
        label_n = Tex("n").scale(0.7).next_to(linha_n, UP, buff=0.1)

        self.play(Create(linha_m), Create(linha_n))
        self.play(Write(label_m), Write(label_n))

        self.play(FadeOut(brace_a_baixo))
        self.play(label_a_baixo.animate.shift(UP * 0.42 + LEFT * 0.18))

        self.wait(1)

        # === TRANSFORMAÇÃO: letras viram palavras, com leve deslocamento ===

        # Criando novos objetos nas posições desejadas
        cateto_b = Tex("cateto").scale(0.7).next_to(lado_b, UP, buff=0.1)
        cateto_c = Tex("cateto").scale(0.7).next_to(lado_c, LEFT, buff=0.1)
        hipo_a = Tex("hipotenusa").scale(0.7).move_to(label_a_baixo)

        self.play(
            TransformMatchingTex(lado_b, cateto_b),
            TransformMatchingTex(lado_c, cateto_c),
            TransformMatchingTex(label_a_baixo, hipo_a)
        )
        self.wait(2)

        # === VOLTA: palavras retornam às letras ===

        letra_b = Tex("b").scale(0.7).move_to((A + C) / 2 + UP * 0.25)
        letra_c = Tex("c").scale(0.7).move_to((A + B) / 2 + LEFT * 0.25)
        letra_a = Tex("a").scale(0.7).move_to(hipo_a)

        self.play(
            TransformMatchingTex(cateto_b, letra_b),
            TransformMatchingTex(cateto_c, letra_c),
            TransformMatchingTex(hipo_a, letra_a)
        )
        self.wait(2)

        triangulo_completo = VGroup(triangulo,ponto_A, ponto_B, ponto_C, ponto_D,label_A, label_B, label_C, label_D,altura, label_altura,linha_m, linha_n,
            label_m, label_n,letra_a, letra_b, letra_c)  # <- depois da transformação reversa)

        self.triangulo_completo = triangulo_completo

        self.play(self.triangulo_completo.animate.shift(LEFT * 2))

                # === Texto explicativo à direita do triângulo ===
        texto_explicativo = Tex(
            r"As letras m e n representam as projeções\\",
            r"dos catetos c e b sobre a hipotenusa e \\"
            r"h é a altura relativa ao lado BC.\\",
            tex_environment="flushleft"
        ).scale(0.6)

        # Posiciona à direita do triângulo
        texto_explicativo.next_to(self.triangulo_completo, RIGHT, buff=0.8).align_to(triangulo, UP)

        # Anima o aparecimento
        self.play(FadeIn(texto_explicativo, shift=RIGHT))
        self.wait(2)


        self.play(FadeOut(explicacao),FadeOut(self.triangulo_completo),FadeOut(texto_explicativo))



        
        # === Vértices do triângulo original ===
        A = LEFT * 2 + UP * 2
        B = LEFT * 3.5 + DOWN * 2
        C = RIGHT * 2.5 + DOWN * 2

        # Triângulo e pontos
        triangulo = Polygon(A, B, C, color=WHITE)
        dot_A, dot_B, dot_C = Dot(A), Dot(B), Dot(C)
        label_A = Tex("A").scale(0.6).next_to(A, UP + LEFT, buff=0.1)
        label_B = Tex("B").scale(0.6).next_to(B, DOWN + LEFT, buff=0.1)
        label_C = Tex("C").scale(0.6).next_to(C, DOWN + RIGHT, buff=0.1)

        # Apresenta triângulo e vértices
        self.play(Create(triangulo))
        self.play(FadeIn(dot_A, dot_B, dot_C))
        self.play(Write(label_A), Write(label_B), Write(label_C))

        # Rótulos dos lados (ajustados para melhor posição)
        meio_AB = interpolate(A, B, 0.5)
        meio_AC = interpolate(A, C, 0.5)
        meio_BC = interpolate(B, C, 0.5)

        label_AB = Tex("c").scale(0.6).move_to(meio_AB + LEFT * 0.2)
        label_AC = Tex("b").scale(0.6).move_to(meio_AC + RIGHT * 0.2 + UP * 0.05)
        label_BC = Tex("a").scale(0.6).move_to(meio_BC + DOWN * 0.2)

        self.play(Write(label_AB), Write(label_AC), Write(label_BC))
        self.wait(1)

        # Ângulos
        ang_A = Angle(Line(A, B), Line(A, C), radius=0.4, color=YELLOW)
        ang_B = Angle(Line(B, C), Line(B, A), radius=0.4, color=GREEN)
        ang_C = Angle(Line(C, A), Line(C, B), radius=0.4, color=BLUE)

        label_alpha = MathTex(r"90^\circ", color=YELLOW).scale(0.6)
        label_beta = MathTex(r"\beta", color=GREEN).scale(0.6)
        label_gamma = MathTex(r"\gamma", color=BLUE).scale(0.6)

        label_alpha.next_to(ang_A, DOWN + RIGHT, buff=0.05).shift(LEFT * 0.25)
        label_beta.next_to(ang_B, UP + RIGHT, buff=0.05)
        label_gamma.next_to(ang_C, UP + LEFT, buff=0.05).shift(LEFT * 0.25 + DOWN * 0.17)

        self.play(Create(ang_A), Write(label_alpha))
        self.play(Create(ang_B), Write(label_beta))
        self.play(Create(ang_C), Write(label_gamma))
        self.wait(1)

        # Cálculo do ponto D (projeção de A na base BC)
        BC = C - B
        AB = A - B
        proj_esc = np.dot(AB, BC) / np.dot(BC, BC)
        D = B + proj_esc * BC

        # Altura AD
        altura = DashedLine(A, D, color=RED)
        ponto_D = Dot(D, color=RED).set_z_index(2)
        label_D = Tex("D").scale(0.5).next_to(ponto_D, UP + RIGHT, buff=0.1)
        label_h = Tex("h", color=RED).scale(0.7).next_to(altura, RIGHT, buff=0.1)

        self.play(Create(altura))
        self.play(FadeIn(ponto_D), Write(label_D))
        self.play(Write(label_h))
        self.wait(1)

        # Projeções m (BD) e n (DC)
        linha_m = Line(B, D, color=PURPLE)
        linha_n = Line(D, C, color=YELLOW)

        label_m = Tex("m", color=PURPLE).scale(0.6).next_to(linha_m, UP, buff=0.1)
        label_n = Tex("n", color=YELLOW).scale(0.6).next_to(linha_n, UP, buff=0.1)

        self.play(Create(linha_m), Create(linha_n))
        self.play(Write(label_m), Write(label_n))
        self.wait(1)

        # Agrupa tudo para mover o triângulo ABC completo para a esquerda
        grupo_ABC = VGroup(
            triangulo, dot_A, dot_B, dot_C, ponto_D,
            label_A, label_B, label_C, label_D,
            label_AB, label_AC, label_BC,
            ang_A, ang_B, ang_C, label_alpha, label_beta, label_gamma,
            altura, label_h, linha_m, linha_n, label_m, label_n
        )

        self.play(grupo_ABC.animate.shift(LEFT * 4 + UP * 0.5).scale(0.7))
        self.wait(1)

        # === Definir os pontos originais ===


        A1 = np.array([-5.57, 1.88, 0])
        B1 = np.array([-6.6, -0.9, 0])
        D1 = np.array([-5.57, -0.9, 0])
        C1 = np.array([-2.43, -0.9, 0])

        # === Criar triângulos originais ===
        trianguloADB = Polygon(A1, B1, D1, fill_color=BLUE, fill_opacity=0.15, stroke_color=BLUE)
        trianguloADC = Polygon(A1, C1, D1, fill_color=YELLOW, fill_opacity=0.15, stroke_color=YELLOW)

        self.play(Create(trianguloADB))
        self.wait(1)
        self.play(trianguloADB.animate.shift(RIGHT * 5))

        # === Triângulo ADB movido ===
        A11 = np.array([-0.57, 1.88, 0])
        B11 = np.array([-1.6, -0.9, 0])
        D11 = np.array([-0.57, -0.9, 0])

        trianguloADB11 = Polygon(A11, B11, D11, fill_color=BLUE, fill_opacity=0.15, stroke_color=BLUE)
        self.play(Create(trianguloADB11))


        # Rótulos dos vértices com coordenadas fixas
        rotulo_A11 = Tex("A").scale(0.5).move_to([-0.8, 2.1, 0])
        rotulo_B11 = Tex("B").scale(0.5).move_to([-1.8, -1.1, 0])
        rotulo_D11 = Tex("D").scale(0.5).move_to([-0.3, -1.1, 0])

        self.play(Write(rotulo_A11), Write(rotulo_B11), Write(rotulo_D11))
        self.wait(1)

        # Rótulos dos lados (fixos no plano)
        rotulo_h = Tex("h", color=RED).scale(0.6).move_to([-0.3, 0.3, 0])
        rotulo_m = Tex("m", color=PURPLE).scale(0.6).move_to([-1.2, -1.3, 0])
        rotulo_b = Tex("c", color=WHITE).scale(0.6).move_to([-1.3, 0.3, 0])

        self.play(Write(rotulo_h), Write(rotulo_m), Write(rotulo_b))
        self.wait(1)


        ang_A11 = Angle(Line(A11, B11), Line(A11, D11), radius=0.4, color=YELLOW).scale(0.7)
        ang_B11 = Angle(Line(B11, D11), Line(B11, A11), radius=0.4, color=GREEN).scale(0.7)
        ang_D11 = Angle(Line(D11, A11), Line(D11, B11), radius=0.4, color=BLUE).scale(0.7)

        # Rótulos posicionados em pontos fixos do plano
        label_alpha11 = MathTex(r"\gamma", color=YELLOW).scale(0.5).move_to([-0.75, 1, 0])
        label_beta11 = MathTex(r"\beta", color=GREEN).scale(0.5).move_to([-1.2, -0.5, 0])
        label_gamma11 = MathTex(r"90^\circ", color=BLUE).scale(0.5).move_to([-0.3, -0.8, 0])

        self.play(Create(ang_A11), Write(label_alpha11))
        self.play(Create(ang_B11), Write(label_beta11))
        self.play(Create(ang_D11), Write(label_gamma11))
        self.wait(1)

        # === Triângulo ADC ===
        self.play(Create(trianguloADC))
        self.wait(1)
        self.play(trianguloADC.animate.shift(RIGHT * 8))

        A12 = np.array([2.43, 1.88, 0])
        C12 = np.array([5.57, -0.9, 0])
        D12 = np.array([2.43, -0.9, 0])

        trianguloADC12 = Polygon(A12, C12, D12, fill_color=YELLOW, fill_opacity=0.15, stroke_color=YELLOW)
        self.play(Create(trianguloADC12))

        rotulo_A12 = Tex("A").scale(0.5).move_to([2.2, 2.1, 0])
        rotulo_C12 = Tex("C").scale(0.5).move_to([5.7, -1.1, 0])
        rotulo_D12 = Tex("D").scale(0.5).move_to([2.5, -1.1, 0])

        self.play(Write(rotulo_A12), Write(rotulo_C12), Write(rotulo_D12))
        self.wait(1)

        rotulo_h2 = Tex("h", color=RED).scale(0.6).move_to([2.2, 0.3, 0])
        rotulo_n = Tex("n", color=YELLOW).scale(0.6).move_to([4.0, -1.3, 0])
        rotulo_c = Tex("b", color=WHITE).scale(0.6).move_to([4.5, 0.3, 0])

        # Aparecer rótulos
        self.play(Write(rotulo_h2), Write(rotulo_n), Write(rotulo_c))
        self.wait(1)

        ang_A12 = Angle(Line(A12, D12), Line(A12, C12), radius=0.4, color=YELLOW).scale(0.7)
        ang_C12 = Angle(Line(C12, A12), Line(C12, D12), radius=0.4, color=GREEN).scale(0.7)
        ang_D12 = Angle(Line(D12, C12), Line(D12, A12), radius=0.4, color=BLUE).scale(0.7)

        # Rótulos posicionados em pontos fixos do plano
        label_alpha12 = MathTex(r"\beta", color=YELLOW).scale(0.5).move_to([2.7, 1.3, 0])
        label_beta12 = MathTex(r"\gamma", color=GREEN).scale(0.5).move_to([5, -0.7, 0])
        label_gamma12 = MathTex(r"90^\circ", color=BLUE).scale(0.5).move_to([2, -0.8, 0])

        self.play(Create(ang_A12), Write(label_alpha12))
        self.play(Create(ang_C12), Write(label_beta12))
        self.play(Create(ang_D12), Write(label_gamma12))
        self.wait(1)

        self.play(
            trianguloADB11.animate.set_fill(opacity=0),
            trianguloADC12.animate.set_fill(opacity=0)
        )
        self.wait(1)


        explicacao3 = Tex(
            r"Os triângulos $\triangle ADB$ e $\triangle ADC$ são semelhantes a $\triangle ABC$, pois possuem três ângulos congruentes.",
            r"Pelo critério $AA \Rightarrow \triangle ADB \sim \triangle ABC$ e $\triangle ADC \sim \triangle ABC$.",
            r"Logo, os lados correspondentes desses triângulos estão em proporção.",
            tex_environment="flushleft"
        ).scale(0.5)

        explicacao3.next_to(grupo_ABC, DOWN, buff=0.3)
        explicacao3.align_to(grupo_ABC, LEFT)

        self.play(Write(explicacao3, run_time=2))
        self.wait(1)

        # === Destaques dos ângulos de ADB com ABC ===
        destaques_adb = [
            SurroundingRectangle(label_gamma11, color=YELLOW, buff=0.1),  # 90° em D (ADB)
            SurroundingRectangle(label_alpha, color=YELLOW, buff=0.1),     # 90° em A (ABC)

            SurroundingRectangle(label_beta11, color=GREEN, buff=0.1),     # beta em B (ADB)
            SurroundingRectangle(label_beta, color=GREEN, buff=0.1),       # beta em B (ABC)

            SurroundingRectangle(label_alpha11, color=BLUE, buff=0.1),     # gamma em A (ADB)
            SurroundingRectangle(label_gamma, color=BLUE, buff=0.1),       # gamma em C (ABC)
        ]

        self.play(*[Create(r) for r in destaques_adb])
        self.wait(2)
        self.play(*[FadeOut(r) for r in destaques_adb])
        self.wait(0.5)

        # === Destaques dos ângulos de ADC com ABC ===
        destaques_adc = [
            SurroundingRectangle(label_gamma12, color=YELLOW, buff=0.1),   # 90° em D (ADC)
            SurroundingRectangle(label_alpha, color=YELLOW, buff=0.1),     # 90° em A (ABC)

            SurroundingRectangle(label_beta12, color=GREEN, buff=0.1),     # gamma em C (ADC)
            SurroundingRectangle(label_gamma, color=GREEN, buff=0.1),      # gamma em C (ABC)

            SurroundingRectangle(label_alpha12, color=BLUE, buff=0.1),     # beta em A (ADC)
            SurroundingRectangle(label_beta, color=BLUE, buff=0.1),        # beta em B (ABC)
        ]

        self.play(*[Create(r) for r in destaques_adc])
        self.wait(2)
        self.play(*[FadeOut(r) for r in destaques_adc])
        self.wait(0.5)

        # === Comparação entre ADB e ADC ===
        explicacao4 = Tex(
            r"Os triângulos $\triangle ADB$ e $\triangle ADC$ também são semelhantes entre si, pois têm os mesmos três ângulos.",
            r"Assim, $\triangle ADB \sim \triangle ADC$.",
            tex_environment="flushleft"
        ).scale(0.5)

        explicacao4.next_to(explicacao3, DOWN, buff=0.25)
        explicacao4.align_to(explicacao3, LEFT)

        self.play(Write(explicacao4, run_time=2))
        self.wait(1)

        destaques_entre_si = [
            SurroundingRectangle(label_gamma11, color=YELLOW, buff=0.1),
            SurroundingRectangle(label_gamma12, color=YELLOW, buff=0.1),

            SurroundingRectangle(label_beta11, color=GREEN, buff=0.1),
            SurroundingRectangle(label_beta12, color=GREEN, buff=0.1),

            SurroundingRectangle(label_alpha11, color=BLUE, buff=0.1),
            SurroundingRectangle(label_alpha12, color=BLUE, buff=0.1),
        ]

        self.play(*[Create(r) for r in destaques_entre_si])
        self.wait(2)
        self.play(*[FadeOut(r) for r in destaques_entre_si])
        self.wait(0.5)

        self.rotulo_h = rotulo_h
        self.rotulo_m = rotulo_m
        self.rotulo_n = rotulo_n
        self.rotulo_h2 = rotulo_h2
        self.rotulo_c = rotulo_c


                # Agrupando elementos do triângulo ADB movido
        grupo_ADBu = VGroup(trianguloADB,
            trianguloADB11,
            ang_A11, ang_B11, ang_D11,
            label_alpha11, label_beta11, label_gamma11, rotulo_A11, rotulo_B11, rotulo_D11, rotulo_h, rotulo_m, rotulo_b
        )

        # Agrupando elementos do triângulo ADC movido
        grupo_ADCu = VGroup(trianguloADC,
            trianguloADC12,
            ang_A12, ang_C12, ang_D12,
            label_alpha12, label_beta12, label_gamma12, rotulo_A12, rotulo_C12, rotulo_D12, rotulo_h2, rotulo_n, rotulo_c
        )


        self.play(FadeOut(explicacao3), FadeOut(explicacao4), FadeOut(grupo_titulo))



        self.play(grupo_ABC.animate.shift(UP * 1.8))
        self.play(grupo_ADBu.animate.shift(UP * 1.8))
        self.play(grupo_ADCu.animate.shift(UP * 1.8))

        self.wait(2)

       

        # === FRAÇÕES DAS RELAÇÕES DE SEMELHANÇA ===

        
        # Texto introdutório abaixo do grupo ABC
        introducao = Tex(
            r"Usando a semelhança entre os triângulos $ADB$ e $ADC$, temos:",
            tex_environment="flushleft"
        ).scale(0.5)

        introducao.next_to(grupo_ABC, DOWN, buff=1)
        introducao.align_to(grupo_ABC, LEFT)

        self.play(Write(introducao))
        self.wait(1)

        # Frases explicativas
        frase1 = MathTex(r"\text{oposto a } \beta \text{ no } ADB \over \text{oposto a } \gamma \text{ no } ADB").scale(0.6)
        frase2 = MathTex(r"\text{oposto a } \beta \text{ no } ADC \over \text{oposto a } \gamma \text{ no } ADC").scale(0.6)
        igual = MathTex("=").scale(0.8)

        fracoes_nomeadas = VGroup(frase1, igual, frase2).arrange(RIGHT, buff=0.4)
        fracoes_nomeadas.next_to(introducao, DOWN, buff=0.4).align_to(introducao, LEFT)

        self.play(Write(frase1))
        self.wait(0.5)
        self.play(Write(igual))
        self.wait(0.3)
        self.play(Write(frase2))
        self.wait(1.5)

        # Transformações das descrições para letras
        fracao1 = MathTex(r"\frac{h}{m}").scale(0.8).move_to(frase1.get_center())
        fracao2 = MathTex(r"\frac{h}{n}").scale(0.8).move_to(frase2.get_center())

        self.play(
            Transform(frase1, fracao1),
            Transform(frase2, fracao2),
        )
        self.wait(1.2)

        # Multiplicação cruzada com linhas transparentes e menores
        segmento1 = Line(
            fracao1[0][0].get_left(), fracao2[0][2].get_right(), 
            color=WHITE, stroke_opacity=0.3, stroke_width=2
        )
        segmento2 = Line(
            fracao1[0][2].get_right(), fracao2[0][0].get_left(), 
            color=WHITE, stroke_opacity=0.3, stroke_width=2
        )

        self.play(Create(segmento1), Create(segmento2), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(segmento1), FadeOut(segmento2), run_time=0.6)

        # Resultado final com seta
        resultado = MathTex(r"\Rightarrow\quad h^2 = m \cdot n").scale(0.9)
        resultado.next_to(fracao2, RIGHT, buff=1.0)
        resultado.set_color_by_tex_to_color_map({"h": RED, "m": PURPLE, "n": YELLOW})
        caixa = SurroundingRectangle(resultado, color=WHITE, buff=0.2)

        self.play(Write(resultado), Create(caixa))
        self.wait(3)

        self.clear()


        

