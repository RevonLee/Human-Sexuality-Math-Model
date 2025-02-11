import numpy as np
import matplotlib.pyplot as plt

def calculate_pleasure(A, S, M, R, L, w1=0.3, w2=0.1, w3=0.4, w4=0.2):
    """
    计算愉悦度评分 P
    A = 外貌评分（0-10）
    S = 性技巧评分（0-10）
    M = 心理 & 生理匹配度（0-1）
    R = 关系稳定性（0-1）
    L = 你对她的喜爱程度（0-10）
    w1, w2, w3, w4 = 各个因素的权重，默认值已设定
    """
    P = (w1 * A + w2 * S + w3 * M + w4 * R) * L
    return P

def plot_pleasure_variation():
    """
    生成愉悦度的影响因素分析图
    """
    A_values = np.linspace(0, 10, 100)  # 外貌从 0 到 10
    S_values = np.linspace(0, 10, 100)  # 性技巧从 0 到 10
    M_values = np.linspace(0, 1, 100)   # 心理/生理匹配从 0 到 1
    R_values = np.linspace(0, 1, 100)   # 关系稳定性从 0 到 1
    L = 9  # 你对她的喜爱程度固定为 9（高）

    # 分别计算 P 值
    P_A = [calculate_pleasure(A, 6, 0.8, 0.8, L) for A in A_values]
    P_S = [calculate_pleasure(8, S, 0.8, 0.8, L) for S in S_values]
    P_M = [calculate_pleasure(8, 6, M, 0.8, L) for M in M_values]
    P_R = [calculate_pleasure(8, 6, 0.8, R, L) for R in R_values]

    # 画图
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 2, 1)
    plt.plot(A_values, P_A, label="P vs 外貌(A)", color="red")
    plt.xlabel("外貌评分 (A)")
    plt.ylabel("愉悦度 (P)")
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(S_values, P_S, label="P vs 性技巧(S)", color="blue")
    plt.xlabel("性技巧评分 (S)")
    plt.ylabel("愉悦度 (P)")
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(M_values, P_M, label="P vs 心理/生理匹配(M)", color="green")
    plt.xlabel("匹配度 (M)")
    plt.ylabel("愉悦度 (P)")
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(R_values, P_R, label="P vs 关系稳定性(R)", color="purple")
    plt.xlabel("关系稳定性 (R)")
    plt.ylabel("愉悦度 (P)")
    plt.legend()

    plt.tight_layout()
    plt.show()

# 运行可视化
if __name__ == "__main__":
    plot_pleasure_variation()
