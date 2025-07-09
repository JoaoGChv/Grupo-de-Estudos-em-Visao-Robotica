"""
filtragem-fourier.py
Implementação de filtros no domínio da frequência usando Transformada de Fourier
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

def aplicar_filtro_fourier(imagem, tipo_filtro='lowpass', cutoff=30):
    """Aplica filtro passa-baixa ou passa-alta via FFT.
    
    Parâmetros:
        imagem (np.ndarray): Imagem de entrada (colorida ou grayscale).
        tipo_filtro (str): 'lowpass' (borrar) ou 'highpass' (nitidez).
        cutoff (int): Raio da região de corte em frequência.
        
    Retorna:
        np.ndarray: Imagem filtrada normalizada em [0, 255].
    """
    # Validar parâmetros
    if cutoff <= 0:
        raise ValueError("cutoff deve ser positivo.")
    
    # Converter para grayscale
    if len(imagem.shape) == 3:
        img_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    else:
        img_gray = imagem.copy()

    rows, cols = img_gray.shape
    if cutoff >= min(rows, cols) // 2:
        raise ValueError("cutoff excede as dimensões da imagem.")

    # Transformada de Fourier
    fft = np.fft.fft2(img_gray)
    fft_shift = np.fft.fftshift(fft)

    # Criar máscara Gaussiana para evitar ringing (Figura 3.24 do livro)
    center_row, center_col = rows // 2, cols // 2
    y, x = np.ogrid[:rows, :cols]
    distancia = np.sqrt((x - center_col)**2 + (y - center_row)**2)
    
    if tipo_filtro == 'lowpass':
        mask = np.exp(-(distancia**2) / (2 * (cutoff**2)))
    elif tipo_filtro == 'highpass':
        mask = 1 - np.exp(-(distancia**2) / (2 * (cutoff**2)))
    else:
        raise ValueError("tipo_filtro deve ser 'lowpass' ou 'highpass'")

    # Aplicar filtro e transformada inversa
    fft_filtrado = fft_shift * mask
    img_filtrada = np.fft.ifft2(np.fft.ifftshift(fft_filtrado))
    img_filtrada = np.abs(img_filtrada)
    img_filtrada = cv2.normalize(img_filtrada, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    return img_filtrada

def visualizar_espectro(fft_shift):
    """Visualiza o espectro de Fourier em log scale."""
    magnitude = np.log(1 + np.abs(fft_shift))
    plt.imshow(magnitude, cmap='gray')
    plt.title('Espectro de Frequência (log)')
    plt.axis('off')
    plt.show()

def visualizar_resultados(original, filtrada1, filtrada2, titulo1, titulo2, salvar=False):
    """Exibe e/ou salva os resultados comparativos."""
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    if len(original.shape) == 3:
        plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    else:
        plt.imshow(original, cmap='gray')
    plt.title('Original')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(filtrada1, cmap='gray')
    plt.title(titulo1)
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(filtrada2, cmap='gray')
    plt.title(titulo2)
    plt.axis('off')
    
    plt.tight_layout()
    
    if salvar:
        plt.savefig('resultados_filtragem.png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # Configurações
    ARQUIVO_IMAGEM = 'predio.jpg' # Se for usar uma imagem diferente, altere aqui!
    CUTOFF_FREQUENCIA = 30
    
    try:
        # Carregar imagem
        img = cv2.imread(ARQUIVO_IMAGEM)
        if img is None:
            raise FileNotFoundError(f"Imagem '{ARQUIVO_IMAGEM}' não encontrada.")
        
        # Processamento
        img_lowpass = aplicar_filtro_fourier(img, 'lowpass', CUTOFF_FREQUENCIA)
        img_highpass = aplicar_filtro_fourier(img, 'highpass', CUTOFF_FREQUENCIA)
        
        # Visualização
        visualizar_resultados(img, img_lowpass, img_highpass,
                            f'Passa-Baixa (cutoff={CUTOFF_FREQUENCIA})',
                            f'Passa-Alta (cutoff={CUTOFF_FREQUENCIA})',
                            salvar=True)
        
        # Visualizar espectro (opcional)
        fft = np.fft.fft2(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
        visualizar_espectro(np.fft.fftshift(fft))
        
    except Exception as e:
        print(f"Erro: {e}")

# Para rodar no terminal: py filtragem-fourier.py