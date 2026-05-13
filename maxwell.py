import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

# 맥(Mac)에서 그래프 창을 별도로 띄우기 위한 필수 설정
matplotlib.use('macosx') 

# 1. 물리 데이터 초기화
size = 200
E = np.zeros(size) # 전기장
B = np.zeros(size) # 자기장

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), num="Maxwell's Wave Simulation")
line_e, = ax1.plot(E, color='red', lw=2, label='Electric Field (E)')
line_b, = ax2.plot(B, color='blue', lw=1.5, label='Magnetic Field (B)')

for ax in [ax1, ax2]:
    ax.set_ylim(-1.5, 1.5)
    ax.grid(True, alpha=0.3)
    ax.legend()

# 2. 맥스웰 방정식의 핵심: 변화가 변화를 만든다
def update(frame):
    global E, B
    
    # 맥스웰-앙페르 법칙: 전기장의 변화(기울기)가 자기장을 생성
    B[:-1] += (E[1:] - E[:-1]) * 0.5
    
    # 패러데이 법칙: 자기장의 변화(기울기)가 전기장을 생성
    E[1:] += (B[1:] - B[:-1]) * 0.5
    
    # 안테나 진동 (스위치봇이 신호를 쏘는 시작점)
    E[0] = np.sin(0.2 * frame)
    
    line_e.set_ydata(E)
    line_b.set_ydata(B)
    return line_e, line_b

# 3. 애니메이션 실행
ani = FuncAnimation(fig, update, frames=200, interval=30, blit=False)
plt.tight_layout()
plt.show()