from manim import *
from pathlib import Path
import os



class cena1(Scene):
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
            "Números e Operações/Álgebra e Funções", font="Fira Sans").scale(0.75)
        titulo_gp.next_to(grupo1, DOWN, buff=0.8)

        self.play(Write(titulo_gp))
        self.wait(1)

        grupo_com_texto = VGroup(grupo1, titulo_gp, inicio)
        self.play(FadeOut(grupo_com_texto))
        t1 = Text("Progressão Aritmética", font="Fira Sans").scale(0.5)
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

        explicacao = Paragraph(
            r"As progressões aritméticas são sequências numéricas em que cada termo subsequente é obtido pela adição de uma constante.",
            r"Para exemplificar, considere a situação ilustrada com os quadrados abaixo.",
            alignment="left",
            line_spacing=0.8,
            font="CMU Serif"
        ).scale(0.35)

        # Posiciona abaixo e alinha à esquerda com o grupo
        explicacao.next_to(grupo2, DOWN, buff=0.3)
        explicacao.align_to(grupo2, LEFT)  # <- ESSENCIAL!

        self.play(Write(explicacao, run_time = 1))
        self.wait(1)

        quadrados = VGroup(*[
            VGroup(
                Square(0.2*i).next_to(DOWN, UP, buff=0).shift(6*LEFT + 1.24**i*RIGHT + i*0.05*RIGHT),
                MathTex(f'{i}').scale(0.7).next_to(DOWN, DOWN, buff=0.3).shift(6*LEFT + 1.24**i*RIGHT + i*0.05*RIGHT),
            )
            for i in range(1, 8, 2)
        ]).add(Tex('...').next_to(DOWN, UP, buff=0)).shift(4.5*LEFT + 1.24**8*RIGHT + 8*0.05*RIGHT)

        self.play(Write(quadrados))
        
        self.play(quadrados.animate.shift(2*LEFT))


        explicacao1 = Paragraph(
            r"Nessa sequência, a diferença constante entre os lados é 2, que representa a razão da progressão.",
            alignment="left",
            line_spacing=0.8,
            font="CMU Serif"
        ).scale(0.35)

        # Posiciona abaixo e alinha à esquerda com o grupo
        explicacao1.next_to(grupo2, DOWN, buff=5)
        explicacao1.align_to(grupo2, LEFT)  # <- ESSENCIAL!

        self.play(Write(explicacao1, run_time = 1))
        self.wait(1)




        explicacao_formula = Paragraph(
            r"Com isso, podemos escrever uma função que calcule o tamanho do lado do n-ésimo quadrado dessa progressão.",
            alignment="left",
            line_spacing=0.8,
            font="CMU Serif"
        ).scale(0.35)

        # Posiciona abaixo e alinha à esquerda com o grupo
        explicacao_formula.next_to(grupo2, DOWN, buff=5.5)
        explicacao_formula.align_to(grupo2, LEFT)  # <- ESSENCIAL!

        self.play(Write(explicacao_formula, run_time = 1))
        self.wait(1)

        funcoes_exemplo = MathTex(r'f(1)=1\\f(2)=3\\f(3)=4\\f(4)=7').scale(0.7).shift(1.5*RIGHT + 0.2*DOWN)
        funcao = MathTex('f(n) = 1 + 2n').scale(0.7).shift(4*RIGHT + 0.5*DOWN)


    
        
        self.play(Write(funcoes_exemplo))
        self.play(Write(funcao))

         # --- Apaga todos os elementos visíveis com fade ---
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)


        duvida = Paragraph(
            r"Como podemos deduzir essa função?",
            alignment="left",
            line_spacing=0.8,
            font="CMU Serif"
        ).scale(0.35)

        self.play(Write(duvida))
        self.wait(1.5)
        self.play(FadeOut(duvida))

        numeros = [
            Tex(f'{i}').scale(0.9).shift(2 * LEFT + i * 0.5 * RIGHT)
            for i in range(1, 8, 2)
        ]
        steps = [
            ArcBetweenPoints(start=start.get_center() + 0.05 * RIGHT,
                             end=end.get_center() + 0.1 * LEFT,
                             color=RED).shift(0.5 * DOWN)
            for start, end in zip(numeros[:-1], numeros[1:])
        ]
        steps_number = [
            Tex(f'+2', color=YELLOW).scale(0.8).next_to(steps[i], DOWN, buff=0.3).shift(0.05 * LEFT)
            for i in range(len(steps))
        ]
        visualizar = VGroup(*numeros, *steps, *steps_number)
        visualizar.shift(UP * 1.2)


        explicacao3 = Paragraph(
            r"A progressão começa em 1 e aumenta de 2 em 2. Para escrever a fórmula, precisamos do primeiro termo da progressão, no caso 1,",
            r"e da diferença entre dois termos, no caso 2. Com isso, podemos ter a seguinte fórmula. Usamos n-1 pois a progressão começa a ",
            r"partir da posição 0 em vez da 1.",
            alignment="left",
            line_spacing=0.8,
            font="CMU Serif"
        ).scale(0.35).shift(UP*2.4)

    
        self.play(Write(explicacao3), run_time = 2)
        self.wait(1.5)


        self.play(Write(visualizar, run_time = 3))
        self.wait(1)

        self.play(visualizar.animate.shift(4.5 * LEFT), run_time = 1.5)



        formula = MathTex(r'f(n) = 1 + 2n').scale(0.7).shift(UP*1.1)
        self.play(Write(formula))

        

        formula_geral = MathTex(r'a_{n} = a_{1} + (n - 1) \cdot r').scale(0.7)
        self.play(Write(formula_geral))
        self.wait(1)

        termos = Tex(
            r'''
            \raggedright
            $a_n$: n-ésimo termo da progressão \\
            $a_1$: primeiro termo da progressão \\
            $n$: posição do termo na progressão \\
            $r$: razão
            '''
        ).scale(0.6).shift(1.2 * DOWN + 0.5*RIGHT)

        self.play(Write(termos))
        self.wait(1)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1.5)


        
        




        




        







        

    