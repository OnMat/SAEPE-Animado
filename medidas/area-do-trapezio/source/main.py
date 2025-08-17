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
            "Grandezas e Medidas", font="Fira Sans").scale(0.75)
        titulo_gp.next_to(grupo1, DOWN, buff=0.8)

        self.play(Write(titulo_gp))
        self.wait(1)

        grupo_com_texto = VGroup(grupo1, titulo_gp, inicio)
        self.play(FadeOut(grupo_com_texto))
        t1 = Text("Área do Trapézio", font="Fira Sans").scale(0.5)
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

        grupo2 = VGroup(linha, t1)
        self.play(grupo2.animate.scale(0.9).to_corner(UP + LEFT), run_time=1.5)
        self.wait(1.5)

                # Texto explicativo ajustado (sem fórmula embutida)
        explicacao = Paragraph(
            r"   A área do trapézio é uma medida que representa a região interna delimitada por seus lados. Um trapézio é um quadrilátero",
            r"que possui dois lados opostos e paralelos, chamados de bases. A altura do trapézio é a distância entre essas duas bases.",
            r"",
            alignment="left",
            line_spacing=0.8, font="CMU Serif"
        ).scale(0.35)

        # Posiciona o parágrafo abaixo de algum grupo anterior
        explicacao.next_to(grupo2, DOWN, buff=0.3)
        explicacao.align_to(grupo2, LEFT)

        self.play(Write(explicacao, run_time=1))
        self.wait(1)

        # === 1. DEFINIÇÃO DOS PONTOS DO TRAPÉZIO ORIGINAL ===
        pontos10 = [[-6, -0.4, 0], [-2, -0.4, 0], [-3.5, 1.1, 0], [-5.5, 1.1, 0]]
        trapezio10 = Polygon(*pontos10, color=WHITE, fill_color=BLUE, fill_opacity=0.3)
        base_maior10 = Line(pontos10[0], pontos10[1], color=WHITE)
        base_menor10 = Line(pontos10[3], pontos10[2], color=WHITE)
        altura10 = Line(pontos10[2], [-3.5, -0.4, 0], color=RED)
        brace_b110 = Brace(base_maior10, DOWN)
        label_b110 = MathTex("b_1", font_size=24).next_to(brace_b110, DOWN, buff=0.1)
        brace_b210 = Brace(base_menor10, UP)
        label_b210 = MathTex("b_2", font_size=24).next_to(brace_b210, UP, buff=0.1)
        label_h10 = MathTex("h", font_size=24).next_to(altura10, LEFT, buff=0.1)

        # === 2. CONSTRUÇÃO DO TRAPÉZIO ===
        self.play(Create(trapezio10))
        self.play(Create(base_maior10), Create(base_menor10))
        self.play(Create(altura10), Write(label_h10))
        self.play(GrowFromCenter(brace_b110), Write(label_b110))
        self.play(GrowFromCenter(brace_b210), Write(label_b210))

        explicacao1 = Paragraph(
            r"   Para calcular a área de um trapézio, utilizamos a média aritmética das bases multiplicada pela altura.",
            r"A fórmula é dada pela expressão abaixo:",
            r"",
            alignment="left",
            line_spacing=0.8, font="CMU Serif"
        ).scale(0.35)

        # Posiciona o parágrafo abaixo de algum grupo anterior
        explicacao1.next_to(label_b110, DOWN, buff=0.3)
        explicacao1.align_to(grupo2, LEFT)
        self.play(Create(explicacao1))
        self.wait(1)

        # === 3. FÓRMULA INICIAL COM TRAPÉZIO ===
        trap_copia10 = trapezio10.copy().scale(0.25).set_fill(BLUE, opacity=0.5)
        inicio10 = MathTex(r"\text{Área}(", font_size=30)
        igual10 = MathTex(r")\ =", font_size=30)
        formula_inicial10 = VGroup(inicio10, trap_copia10, igual10).arrange(RIGHT, buff=0.2)
        formula_inicial10.to_corner(DOWN + LEFT, buff=0.8)

        trap_anim10 = trapezio10.copy()
        trap_anim10.generate_target()
        trap_anim10.target.scale(0.25)
        trap_anim10.target.move_to(trap_copia10.get_center())

        self.play(Write(inicio10))
        self.play(MoveToTarget(trap_anim10), run_time=2)
        self.play(Write(igual10))
        self.remove(trap_anim10)
        self.add(trap_copia10)
        self.wait()

                # === Fórmula final em LaTeX ao lado do "=" ===
        formula_area10 = MathTex(
            r"\frac{(b_1 + b_2) \cdot h}{2}", font_size=32
        )

        # Posiciona ao lado do sinal de igual
        formula_area10.next_to(igual10, RIGHT, buff=0.3)  # você pode ajustar o buff

        # Adiciona na cena com animação
        self.play(Write(formula_area10))
        self.wait(2)

        # Agrupa a expressão completa se quiser reposicionar depois
        expressao_completa = VGroup(inicio10, trap_copia10, igual10, formula_area10)


        # --- Apaga todos os elementos visíveis com fade ---
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

        # Título com linha animada - DEMONSTRAÇÃO (Variáveis com índice 6)
        t6 = Text("Demonstração", font="Fira Sans").scale(0.5)
        self.play(Write(t6, run_time=2))
        self.wait(0.5)

        linha6 = Line(
            start=t6.get_bottom() + DOWN * 0.2 + LEFT * t6.width / 2,
            end=t6.get_bottom() + DOWN * 0.2 + RIGHT * t6.width / 2,
            stroke_width=6,
        )
        linha6.set_color(RED)

        def atualizar_linha6(obj, dt):
            tempo = self.time
            nova_cor = interpolate_color(RED, BLUE, (np.sin(tempo * 2) + 1) / 2)
            obj.set_color(nova_cor)

        linha6.add_updater(atualizar_linha6)
        self.play(FadeIn(linha6))
        self.wait(1)

        grupo_titulo6 = VGroup(t6, linha6)
        self.play(grupo_titulo6.animate.scale(0.9).to_corner(UL), run_time=1.5)
        self.wait(1)




        # === 1. DEFINIÇÃO DOS PONTOS DO TRAPÉZIO ORIGINAL ===
        pontos = [[-3, 0, 0], [2, 0, 0], [0, 3, 0], [-2, 3, 0]]
        trapezio = Polygon(*pontos, color=WHITE, fill_color=BLUE, fill_opacity=0.3)
        base_maior = Line(pontos[0], pontos[1], color=WHITE)
        base_menor = Line(pontos[3], pontos[2], color=WHITE)
        altura = Line(pontos[2], [0, 0, 0], color=RED)
        brace_b1 = Brace(base_maior, DOWN)
        label_b1 = MathTex("b_1", font_size=36).next_to(brace_b1, DOWN, buff=0.1)
        brace_b2 = Brace(base_menor, UP)
        label_b2 = MathTex("b_2", font_size=36).next_to(brace_b2, UP, buff=0.1)
        label_h = MathTex("h", font_size=36).next_to(altura, LEFT, buff=0.1)

        # === 2. CONSTRUÇÃO DO TRAPÉZIO ===
        self.play(Create(trapezio))
        self.play(Create(base_maior), Create(base_menor))
        self.play(Create(altura), Write(label_h))
        self.play(GrowFromCenter(brace_b1), Write(label_b1))
        self.play(GrowFromCenter(brace_b2), Write(label_b2))

        # === 3. FÓRMULA INICIAL COM TRAPÉZIO ===
        trap_copia = trapezio.copy().scale(0.25).set_fill(BLUE, opacity=0.5)
        inicio = MathTex(r"\text{Área}(", font_size=36)
        igual = MathTex(r")\ =", font_size=36)
        formula_inicial = VGroup(inicio, trap_copia, igual).arrange(RIGHT, buff=0.2)
        formula_inicial.to_corner(DOWN + LEFT, buff=0.8)

        trap_anim = trapezio.copy()
        trap_anim.generate_target()
        trap_anim.target.scale(0.25)
        trap_anim.target.move_to(trap_copia.get_center())

        self.play(Write(inicio))
        self.play(MoveToTarget(trap_anim), run_time=2)
        self.play(Write(igual))
        self.remove(trap_anim)
        self.add(trap_copia)
        self.wait()

        # === 4. ROTAÇÃO DO SEGMENTO AE ===
        A_coords = [-3, 0, 0]
        E_coords = [-2.505, 1.5, 0]
        D_coords = [-2, 3, 0]
        C_coords = [0, 3, 0]
        ponto_A = Dot(A_coords, color=RED)
        ponto_E = Dot(E_coords, color=BLUE)
        segmento_AE = Line(A_coords, E_coords, color=RED)
        self.play(Create(ponto_E))
        self.play(Create(segmento_AE), FadeIn(ponto_A))
        grupo = VGroup(segmento_AE, ponto_A)

        trapezio1 = Polygon(A_coords, [2, 0, 0], C_coords, E_coords, color=WHITE, fill_color=BLUE, fill_opacity=0.3)
        self.play(Rotate(grupo, angle=-PI, about_point=ponto_E.get_center()))
        self.wait()

        triangulo_EDC = Polygon(E_coords, D_coords, C_coords, color=BLUE, fill_color=BLUE, fill_opacity=0.3)
        self.play(Create(triangulo_EDC), FadeOut(VGroup(segmento_AE, base_menor, brace_b2, label_b2)), 
                  FadeIn(trapezio1), FadeOut(trapezio), FadeOut(ponto_A))
        self.wait()
        self.play(Rotate(triangulo_EDC, angle=PI, about_point=ponto_E.get_center()))
        self.wait()

        # === 7. BRACE NOVO PARA BASE b₂ ===
        ponto_inicio = [-5, 0, 0]
        ponto_fim = [-3, 0, 0]
        base_manual = Line(ponto_inicio, ponto_fim, color=WHITE)
        brace_b2_manual = Brace(base_manual, direction=DOWN)
        label_b2_manual = MathTex("b_2", font_size=36).next_to(brace_b2_manual, DOWN, buff=0.2)
        self.play(Create(base_manual))
        self.play(GrowFromCenter(brace_b2_manual), Write(label_b2_manual))
        self.wait()

        grupo10 = VGroup(brace_b2_manual, label_b2_manual)
        ponto_inicio1 = [-5, 0, 0]
        ponto_fim1 = [2, 0, 0]
        base_manual1 = Line(ponto_inicio1, ponto_fim1, color=WHITE)
        brace_b2_manual1 = Brace(base_manual1, direction=DOWN)
        label_b2_manual1 = MathTex("(b_1 + b_2)", font_size=36).next_to(brace_b2_manual1, DOWN, buff=0.2)
        grupo11 = VGroup(brace_b2_manual1, label_b2_manual1)

        self.play(FadeOut(brace_b1), FadeOut(label_b1), FadeOut(ponto_E))

        self.play(ReplacementTransform(grupo10, grupo11))




        # === 8. TRIÂNGULO FINAL E FÓRMULA COMPLETA ===
        tri_real = Polygon([-5, 0, 0], [2, 0, 0], [0, 3, 0], color=YELLOW, fill_color=YELLOW, fill_opacity=0.1)
        self.play(Create(tri_real))

        tri_copia = tri_real.copy().scale(0.25)
        area_triangulo = MathTex(r"\text{Área}(", font_size=36)
        fecha = MathTex(") = ", font_size=36)
        formula_final = VGroup(area_triangulo, tri_copia, fecha).arrange(RIGHT, buff=0.2)
        formula_final.next_to(formula_inicial, RIGHT, buff=0.4)

        tri_anim = tri_real.copy()
        tri_anim.generate_target()
        tri_anim.target.scale(0.25)
        tri_anim.target.move_to(tri_copia.get_center())

        self.play(MoveToTarget(tri_anim), run_time=2)
        self.play(Write(area_triangulo), Write(fecha))
        self.remove(tri_anim)
        self.add(tri_copia)

    
                # --- ADICIONANDO EXPRESSÃO COM "base × altura" ---
        base1 = MathTex(r"\text{base}", font_size=36)
        produto = MathTex(r"\times", font_size=34)
        altura1 = MathTex(r"\text{altura}", font_size=36)

        formula_final1 = VGroup(base1, produto, altura1).arrange(RIGHT, buff=0.2)
        formula_final1.next_to(formula_final, RIGHT, buff=0.4)
        formula_final1.shift(UP * 0.33)

        # Linha de divisão e denominador
        largura_linha = 2.2
        linha_divisao = Line(LEFT * largura_linha / 2, RIGHT * largura_linha / 2)
        linha_divisao.next_to(formula_final1, DOWN, buff=0.2)
        denominador = MathTex("2", font_size=30)
        denominador.next_to(linha_divisao, DOWN, buff=0.15)

        grupo_expressao = VGroup(formula_final1, linha_divisao, denominador)

        self.play(Create(formula_final1), Create(linha_divisao), Write(denominador))
        self.wait(1)

                # --- Cópias dos rótulos originais ---
        b1b2_copia = label_b2_manual1.copy()
        h_copia = label_h.copy()
        self.add(b1b2_copia, h_copia)

        # --- Definir distâncias personalizadas ---
        deslocamento_b1b2_x = 0.4          # quanto mover o (b_1 + b_2) para a direita
        distancia_desejada_produto = 0.9  # entre b1b2 e ×
        distancia_desejada_h = 0.35       # entre × e h

        # --- Calcular posições finais ---
        destino_b1b2 = base1.get_center() + RIGHT * deslocamento_b1b2_x
        destino_produto = destino_b1b2 + RIGHT * distancia_desejada_produto
        destino_h = destino_produto + RIGHT * distancia_desejada_h

        # --- Posição inicial do produto: mais próximo de b1b2 ---
        produto.move_to(destino_b1b2 + RIGHT * 0.2)  # ponto de partida do ×
        self.add(produto)

        # --- Animação sincronizada com movimento real do × ---
        self.play(
            FadeOut(base1),
            FadeOut(altura1),
            b1b2_copia.animate.move_to(destino_b1b2),
            produto.animate.move_to(destino_produto),
            h_copia.animate.move_to(destino_h)
        )
        self.wait(0.5)

        # --- Agrupar nova expressão com linha e denominador ---
        nova_expressao = VGroup(b1b2_copia, produto, h_copia)
        nova_expressao_with_div = VGroup(nova_expressao, linha_divisao, denominador)
        self.wait(2)



        # --- Apaga todos os elementos visíveis com fade ---
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1.5)
