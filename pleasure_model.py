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

# 测试案例
if __name__ == "__main__":
    # 设定测试值
    A, S, M, R, L = 8, 6, 0.9, 0.8, 9
    score = calculate_pleasure(A, S, M, R, L)
    print(f"计算出的愉悦度评分: {score}")
