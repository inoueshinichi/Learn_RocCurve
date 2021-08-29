def animate(nframe):
    global num_frame
    sys.stdout.write(str(int(float(nframe)/num_frame*100)) + "%, ") 
    
    plt.clf()
    xmin = 10
    xmax = 45

    # xの分割数
    sx = 200

    # x軸生成
    xx = np.linspace(xmin, xmax, sx)

    mu1 = 20 
    mu2 = 30
    
    sd1 = .5 * (11-nframe)
    sd2 = 4
    
    # 分布の準備
    x1 = st.norm.pdf(xx, loc=mu1, scale=sd1)
    x2 = st.norm.pdf(xx, loc=mu2, scale=sd2)
    cx1 = st.norm.cdf(xx, loc=mu1, scale=sd1)
    cx2 = st.norm.cdf(xx, loc=mu2, scale=sd2)

    # Graph描画
    plt.subplot(211)
    plt.title("Density curve. sd1=%.3f"%sd1)
    plt.xlim(xmin, xmax)
    plt.ylim(0,0.22)
    plt.plot(xx,x1,linewidth=2, zorder = 200)
    plt.plot(xx,x2,linewidth=2, zorder = 200)

    auc = mt.auc(cx2,cx1)
    plt.subplot(212)
    plt.title("ROC Curve. auc=%f"%(auc))
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.plot(cx2,cx1, linewidth=2)


num_frame = 10
fig = plt.figure(figsize=(7,10))
anim = ani.FuncAnimation(fig, animate, frames=num_frame, blit=True)
anim.save('ROC_curve_auc.gif', writer='imagemagick', fps=1, dpi=64)