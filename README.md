# Grupo de Estudos de Visão Robótica

## Apresentações

### Formação de Imagens (Capítulo 2 - Szeliski)

- **Slides**: https://www.canva.com/design/DAGi32RfMY0/vUnwCS2_B-dYyu2I1_Sd0g/view?utm_content=DAGi32RfMY0&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h967130f7f4

### Geometria Projetiva e Transformações de 2D (Capítulo 2 - Hartley)

- **Slides**: https://www.canva.com/design/DAGlyB6r3N8/w_FmtqjLsUW8LvyjSNbPeA/view?utm_content=DAGlyB6r3N8&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hc542fe47e1

- **Material mencionado**: Repositório MapMap (https://github.com/mapmapteam)

### Low level features e Corner detection

- **Slides**: [pdf's](/home/lavi/gp-visao-robotica/Grupo-de-Estudos-em-Visao-Robotica/slides)

## Ideias de projetos

[Early Vision](https://www.sciencedirect.com/topics/engineering/early-vision)


### Edge detection

Apresentar uma aplicação com a imagem gradiente (módulo e fase) e a detecção de bordas usando o algoritmo de Canny. Visualizar os gradientes $G_x$, $G_y$, a magnitude e a fase do gradiente.

1. Imagem gradiente
2. Algoritmo de Canny 

### Corner detection

Apresentar uma aplicação com a detecção de pontos de interesse usando a resposta de Harris, a de Shi-Tomasi e o método FAST. Visualizar as componentes intermediárias do cálculo da resposta de canto.

1. Detector de Harris
2. Shi-Tomasi
3. FAST

### Tracking de objetos

Apresentar uma aplicação de acompanhamento de objetos usando um dos métodos abaixo:

1. [Mean-shift](https://www.cse.psu.edu/~rtc12/CSE598G/introMeanShift.pdf)
2. [Cam-shift](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5543787)
3. [Tracking-Learning-Detection (TLD)](http://vision.stanford.edu/teaching/cs231b_spring1415/papers/Kalal-PAMI.pdf)

### Mapa de disparidades

Criar uma aplicação que receba duas imagens (estereoscópicas) e apresente o mapa de disparidades.

1. Implementar um método Local, baseado em correlação cruzada
2. Implementar um método Global, usando programação dinâmica

### Bird-eye-view

Apresentar uma aplicação para a correção de visualização de imagens de planos.

1. Cálculo da homografia
2. Implementar a interpolação da imagem (Bilinear)
3. Transformação da imagem

### Calibração de câmeras

Apresentar uma aplicação para a calibração de câmeras usando o método de Zhang.

1. Calcular matriz de parâmetros intrínsecos (linear)
2. Calcular matriz de parâmetros intrínsecos (não-linear)
3. Retificação de imagem

### Calibração de sistema estereoscópico

1. Calcular a matriz de parâmetros extrínsecos e corrigir as imagens para um sistema retificado.


