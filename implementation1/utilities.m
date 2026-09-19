function plot_dtft(x)
    N = max(length(x), 100000);
    
    X = fft(x, N);
    X = fftshift(X);
    
    w = (-N/2:N/2-1) * (2*pi/N);
    
    figure;
    plot(w, abs(X));
    grid on;
    
    xlim([-pi pi]);
    xticks([-pi, -3*pi/4, -pi/2, -pi/4, 0, pi/4, pi/2, 3*pi/4, pi]);
    
    ylabel('|X(\omega)|');
    xlabel('\omega (rad/sample)');
end


% Example usage
h = [1, 2, 3, 2, 1];
plot_dtft(h);
