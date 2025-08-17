from manim import *
import itertools
import numpy as np

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
            "Estatística, Probabilidade e Análise Combinatória", font="Fira Sans").scale(0.75)
        titulo_gp.next_to(grupo1, DOWN, buff=0.8)

        self.play(Write(titulo_gp))
        self.wait(1)

        grupo_com_texto = VGroup(grupo1, titulo_gp, inicio)
        self.play(FadeOut(grupo_com_texto))
        t1 = Text("Análise Combinatória", font="Fira Sans").scale(0.5)
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

        # ---------- COMBINAÇÃO ----------
        novo_titulo = Text("Combinação", font="Fira Sans").scale(0.5)
        novo_titulo.move_to(t1.get_center())

        nova_linha = Line(
            start=novo_titulo.get_bottom() + DOWN * 0.2 + LEFT * novo_titulo.width / 2,
            end=novo_titulo.get_bottom() + DOWN * 0.2 + RIGHT * novo_titulo.width / 2,
            stroke_width=6
        ).set_color(linha.get_color())

        self.play(Transform(t1, novo_titulo), Transform(linha, nova_linha))
        self.wait(0.5)

        self.play(FadeOut(t1), FadeOut(linha))
        self.wait(1)

        grupo_titulo = VGroup(novo_titulo, nova_linha)
        self.play(grupo_titulo.animate.scale(0.9).to_corner(UL))
        self.wait(1)

        explicacao_combinacao = Paragraph(
            r"   Em uma combinação, escolhemos elementos de um conjunto, mas a ordem desses elementos não importa.",
            r"Por exemplo, se escolhemos as letras A e B, isso é considerado o mesmo que escolher B e A.",
            r"",
            r"   A fórmula para calcular o número de combinações de n elementos tomados k a k é:",
            alignment="left", line_spacing=0.8, font="CMU Serif"
        ).scale(0.35)

        formula_combinacao = MathTex(r"C(n, k) = \dfrac{n!}{k!(n-k)!}").scale(0.8)

        explicacao_variaveis_comb = Paragraph(
            r"n é o número total de elementos, k é a quantidade escolhida, e ! indica fatorial.",
            alignment="left", line_spacing=0.8, font="CMU Serif"
        ).scale(0.3)

        # Correção: agora usamos novo_titulo como referência
        explicacao_combinacao.next_to(grupo_titulo, DOWN, buff=0.3).align_to(grupo_titulo, LEFT)
        self.play(Write(explicacao_combinacao))
        self.wait(1)

        formula_combinacao.next_to(explicacao_combinacao, DOWN, buff=0.4).align_to(explicacao_combinacao, LEFT)
        self.play(Write(formula_combinacao))
        self.wait(1.2)

        explicacao_variaveis_comb.next_to(formula_combinacao, DOWN, buff=0.3).align_to(formula_combinacao, LEFT)
        self.play(Write(explicacao_variaveis_comb))
        self.wait(1.2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

        # ---------- BOLINHAS ----------
        cores = [RED, GREEN, BLUE, YELLOW, PURPLE]
        nomes = ["A", "B", "C", "D", "E"]
        bolas_base = []

        for cor, nome in zip(cores, nomes):
            bola = Circle(radius=0.12, color=WHITE, fill_color=cor, fill_opacity=1)
            label = Text(nome, font_size=18).next_to(bola, UP, buff=0.05)
            grupo = VGroup(label, bola)
            bolas_base.append(grupo)

        base_group = VGroup(*bolas_base).arrange(RIGHT, buff=0.3).move_to(ORIGIN)
        self.play(FadeIn(base_group))
        self.wait(1)
        self.play(base_group.animate.shift(UP * 2.8))  # ← Ajuste de altura

        # ---------- COMBINAÇÕES ----------
        combinacoes = list(itertools.combinations(bolas_base, 2))
        titulo_comb = Text("Combinações (ordem não importa)", font_size=28).next_to(base_group, DOWN, buff=0.3)
        self.play(Write(titulo_comb))

        combinacao_group = VGroup()
        for i, (a, b) in enumerate(combinacoes):
            copia_a, copia_b = a.copy(), b.copy()
            par = VGroup(copia_a, copia_b).arrange(RIGHT, buff=0.25)

            linha_idx = i // 6
            coluna = i % 6
            par.move_to(LEFT * 4.2 + RIGHT * 1.8 * coluna + DOWN * (1.1 + 0.9 * linha_idx))
            combinacao_group.add(par)

        self.play(LaggedStartMap(FadeIn, combinacao_group, shift=DOWN, lag_ratio=0.03))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

        # ---------- ARRANJO ----------
        novo_titulo1 = Text("Arranjo", font="Fira Sans").scale(0.5)
        

        nova_linha1 = Line(
            start=novo_titulo1.get_bottom() + DOWN * 0.2 + LEFT * novo_titulo1.width / 2,
            end=novo_titulo1.get_bottom() + DOWN * 0.2 + RIGHT * novo_titulo1.width / 2,
            stroke_width=6
        ).set_color(linha.get_color())

        self.play(Write(novo_titulo1), Write(nova_linha1))
        self.wait(1)

        grupo_titulo1 = VGroup(novo_titulo1, nova_linha1)
        self.play(grupo_titulo1.animate.scale(0.9).to_corner(UL))
        self.wait(1)

        explicacao_arranjo = Paragraph(
            r"   Os arranjos representam a seleção de elementos de um conjunto em que a ordem dos escolhidos faz diferença.",
            r"Ou seja, escolher A e B não é o mesmo que escolher B e A.",
            r"",
            r"   A fórmula do arranjo simples de n elementos tomados k a k é:",
            alignment="left", line_spacing=0.8, font="CMU Serif"
        ).scale(0.35)

        formula_arranjo = MathTex(r"A(n, k) = \dfrac{n!}{(n - k)!}").scale(0.8)

        explicacao_variaveis_arranjo = Paragraph(
            r"n é o total de elementos, k é o número de posições, e ! representa o fatorial.",
            alignment="left", line_spacing=0.8, font="CMU Serif"
        ).scale(0.3)

        explicacao_arranjo.next_to(grupo_titulo1, DOWN, buff=0.3).align_to(grupo_titulo1, LEFT)
        self.play(Write(explicacao_arranjo))
        self.wait(1)

        formula_arranjo.next_to(explicacao_arranjo, DOWN, buff=0.4).align_to(explicacao_arranjo, LEFT)
        self.play(Write(formula_arranjo))
        self.wait(1.2)

        explicacao_variaveis_arranjo.next_to(formula_arranjo, DOWN, buff=0.3).align_to(formula_arranjo, LEFT)
        self.play(Write(explicacao_variaveis_arranjo))
        self.wait(1.2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

        arranjos = list(itertools.permutations(bolas_base, 2))
        titulo_arr = Text("Arranjos (ordem importa, sem repetição)", font_size=28).to_edge(UP)
        self.play(Write(titulo_arr))

        arranjo_group = VGroup()
        for i, (a, b) in enumerate(arranjos):
            copia_a, copia_b = a.copy(), b.copy()
            par = VGroup(copia_a, copia_b).arrange(RIGHT, buff=0.25)

            linha_idx = i // 8
            coluna = i % 8
            par.move_to(LEFT * 5 + RIGHT * 1.5 * coluna + DOWN * (1.1 + 0.9 * linha_idx))
            arranjo_group.add(par)

        self.play(LaggedStartMap(FadeIn, arranjo_group, shift=DOWN, lag_ratio=0.02))
        self.wait(2)
        self.play(FadeOut(arranjo_group), FadeOut(titulo_arr), FadeOut(base_group))

        # ---------- PERMUTAÇÃO ----------
        novo_titulo2 = Text("Permutação", font="Fira Sans").scale(0.5)
        

        nova_linha2 = Line(
            start=novo_titulo2.get_bottom() + DOWN * 0.2 + LEFT * novo_titulo2.width / 2,
            end=novo_titulo2.get_bottom() + DOWN * 0.2 + RIGHT * novo_titulo2.width / 2,
            stroke_width=6
        ).set_color(linha.get_color())

        self.play(Write(novo_titulo2), Write(nova_linha2))
        self.wait(1)

        grupo_titulo2 = VGroup(novo_titulo2, nova_linha2)
        self.play(grupo_titulo2.animate.scale(0.9).to_corner(UL))
        self.wait(1)

        explicacao_permutacao = Paragraph(
            r"   As permutações são casos especiais de arranjos em que usamos todos os elementos disponíveis.",
            r"A ordem importa, então organizar A, B e C é diferente de organizar C, B e A.",
            r"",
            r"   A fórmula da permutação de n elementos distintos é:",
            alignment="left", line_spacing=0.8, font="CMU Serif"
        ).scale(0.35)

        formula_permutacao = MathTex(r"P(n) = n!").scale(0.8)

        explicacao_variaveis_perm = Paragraph(
            r"n representa o número total de elementos distintos, e ! é o fatorial.",
            alignment="left", line_spacing=0.8, font="CMU Serif"
        ).scale(0.3)

        explicacao_permutacao.next_to(grupo_titulo2, DOWN, buff=0.3).align_to(grupo_titulo2, LEFT)
        self.play(Write(explicacao_permutacao))
        self.wait(1)

        formula_permutacao.next_to(explicacao_permutacao, DOWN, buff=0.4).align_to(explicacao_permutacao, LEFT)
        self.play(Write(formula_permutacao))
        self.wait(1.2)

        explicacao_variaveis_perm.next_to(formula_permutacao, DOWN, buff=0.3).align_to(formula_permutacao, LEFT)
        self.play(Write(explicacao_variaveis_perm))
        self.wait(1.2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

        cores_perm = [RED, GREEN, BLUE]
        nomes_perm = ["A", "B", "C"]
        bolas_perm = []

        for cor, nome in zip(cores_perm, nomes_perm):
            bola = Circle(radius=0.12, color=WHITE, fill_color=cor, fill_opacity=1)
            label = Text(nome, font_size=18).next_to(bola, UP, buff=0.05)
            grupo = VGroup(label, bola)
            bolas_perm.append(grupo)

        titulo_perm = Text("Permutações de 3 bolinhas coloridas (3!)", font_size=30).to_edge(UP)
        self.play(Write(titulo_perm))

        perm_group = VGroup()
        permutacoes = list(itertools.permutations(bolas_perm, 3))

        for i, (a, b, c) in enumerate(permutacoes):
            tripla = VGroup(a.copy(), b.copy(), c.copy()).arrange(RIGHT, buff=0.25)
            linha_idx = i // 3
            coluna = i % 3
            tripla.move_to(LEFT * 2.8 + RIGHT * 2.5 * coluna + DOWN * (1.5 + 1.2 * linha_idx))
            perm_group.add(tripla)

        self.play(LaggedStartMap(FadeIn, perm_group, shift=DOWN, lag_ratio=0.05))
        self.wait(2)
        self.play(FadeOut(perm_group), FadeOut(titulo_perm))

        self.clear()

