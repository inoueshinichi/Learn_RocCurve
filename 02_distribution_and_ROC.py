def animate(nframe):
    global num_frame
    sys.stdout.write(str(int(float(nframe)/num_frame*100)) + "%, ") 
    
    plt.clf()
    # xの最小値、最大値
    xmin = 15
    xmax = 45

    # xの分割数
    sx = num_frame * 2

    # 現在位置
    pos = nframe * 2

    # x軸生成
    xx = np.linspace(xmin, xmax, sx)

    # 分布の準備
    x1 = st.norm.pdf(xx, loc=25, scale=2)
    x2 = st.norm.pdf(xx, loc=30, scale=4)
    cx1 = st.norm.cdf(xx, loc=25, scale=2)
    cx2 = st.norm.cdf(xx, loc=30, scale=4)

    # Graph描画
    plt.subplot(311)
    plt.title("Density curve. x=%d"%xx[pos])
    plt.xlim(xmin, xmax)
    plt.ylim(0,0.22)
    plt.plot(xx,x1,linewidth=2, zorder = 200)
    plt.plot(xx,x2,linewidth=2, zorder = 200)
    plt.plot([xx[pos], xx[pos]], [0,1], "k", linewidth=2)
    plt.fill_between(xx[0:pos],x1[0:pos], color="lightblue", zorder = 10)
    plt.fill_between(xx[0:pos],x2[0:pos], color="lightgreen", zorder = 100)

    plt.subplot(312)
    plt.title("Cumulative curve. x=%d"%xx[pos])
    plt.xlim(xmin, xmax)
    plt.ylim(0,1)
    plt.plot(xx,cx1,linewidth=2)
    plt.plot(xx,cx2,linewidth=2)
    plt.plot([xx[pos], xx[pos]], [0,1], "k", linewidth=2, zorder=50)
    plt.scatter(xx[pos],cx1[pos], c="b", s=30, zorder=100)
    plt.scatter(xx[pos],cx2[pos], c="g", s=30, zorder=100)


    plt.subplot(313)
    plt.title("ROC Curve. 1-e1=%.3f, e2=%.3f"%(cx1[pos],cx2[pos]))
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.plot(cx2,cx1, linewidth=2)
    plt.scatter(cx2[pos],cx1[pos], c="b", s=30, zorder=100)

num_frame = 100
fig = plt.figure(figsize=(7,15))
anim = ani.FuncAnimation(fig, animate, frames=num_frame, blit=True)
anim.save('ROC_curve1.gif', writer='imagemagick', fps=5, dpi=64)