/* ==========================================
   TransitOps Operations Charting Engine
   ========================================== */

document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById('operationsChart');
    if (!ctx) return;

    // Detect if dark mode is active to apply correct grid colors
    const isDark = document.documentElement.getAttribute("data-bs-theme") === "dark";
    const gridColor = isDark ? "rgba(255, 255, 255, 0.06)" : "rgba(15, 23, 42, 0.05)";
    const textColor = isDark ? "#94a3b8" : "#475569";

    // Setup linear gradients for lines and fills
    const canvasContext = ctx.getContext('2d');
    
    // Indigo Gradient
    const primaryGradient = canvasContext.createLinearGradient(0, 0, 0, 300);
    primaryGradient.addColorStop(0, 'rgba(99, 102, 241, 0.35)');
    primaryGradient.addColorStop(1, 'rgba(99, 102, 241, 0.01)');

    // Emerald/Success Gradient
    const secondaryGradient = canvasContext.createLinearGradient(0, 0, 0, 300);
    secondaryGradient.addColorStop(0, 'rgba(16, 185, 129, 0.25)');
    secondaryGradient.addColorStop(1, 'rgba(16, 185, 129, 0.01)');

    // Instantiation
    const operationsChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [
                {
                    label: 'Trips Completed',
                    data: [65, 78, 72, 89, 95, 45, 55],
                    borderColor: '#6366f1',
                    borderWidth: 3,
                    backgroundColor: primaryGradient,
                    fill: true,
                    tension: 0.4,
                    pointBackgroundColor: '#6366f1',
                    pointHoverRadius: 7,
                    pointHoverBackgroundColor: '#ffffff',
                    pointHoverBorderColor: '#6366f1',
                    pointHoverBorderWidth: 3
                },
                {
                    label: 'Active Vehicles',
                    data: [32, 35, 33, 38, 41, 28, 30],
                    borderColor: '#10b981',
                    borderWidth: 2,
                    backgroundColor: secondaryGradient,
                    fill: true,
                    tension: 0.4,
                    pointBackgroundColor: '#10b981',
                    pointHoverRadius: 6,
                    pointHoverBackgroundColor: '#ffffff',
                    pointHoverBorderColor: '#10b981',
                    pointHoverBorderWidth: 2,
                    borderDash: [5, 5]
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        font: {
                            family: "'Outfit', sans-serif",
                            size: 12,
                            weight: '500'
                        },
                        color: textColor,
                        boxWidth: 15,
                        usePointStyle: true,
                        pointStyle: 'circle'
                    }
                },
                tooltip: {
                    backgroundColor: isDark ? '#0f172a' : '#ffffff',
                    titleColor: isDark ? '#ffffff' : '#0f172a',
                    bodyColor: isDark ? '#cbd5e1' : '#475569',
                    borderColor: isDark ? 'rgba(255,255,255,0.1)' : 'rgba(15,23,42,0.08)',
                    borderWidth: 1,
                    cornerRadius: 8,
                    padding: 12,
                    titleFont: {
                        family: "'Outfit', sans-serif",
                        weight: '700'
                    },
                    bodyFont: {
                        family: "'Outfit', sans-serif"
                    },
                    displayColors: true,
                    callbacks: {
                        labelColor: function(context) {
                            return {
                                borderColor: context.dataset.borderColor,
                                backgroundColor: context.dataset.borderColor,
                                borderWidth: 2
                            };
                        }
                    }
                }
            },
            scales: {
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: textColor,
                        font: {
                            family: "'Outfit', sans-serif",
                            size: 11
                        }
                    }
                },
                y: {
                    grid: {
                        color: gridColor
                    },
                    ticks: {
                        color: textColor,
                        font: {
                            family: "'Outfit', sans-serif",
                            size: 11
                        }
                    }
                }
            }
        }
    });

    // Listen for theme toggle clicks to update colors dynamically
    const toggle = document.getElementById("themeToggle");
    if (toggle) {
        toggle.addEventListener("click", function() {
            setTimeout(function() {
                const isDarkNow = document.documentElement.getAttribute("data-bs-theme") === "dark";
                const newGridColor = isDarkNow ? "rgba(255, 255, 255, 0.06)" : "rgba(15, 23, 42, 0.05)";
                const newTextColor = isDarkNow ? "#94a3b8" : "#475569";

                operationsChart.options.scales.y.grid.color = newGridColor;
                operationsChart.options.scales.x.ticks.color = newTextColor;
                operationsChart.options.scales.y.ticks.color = newTextColor;
                operationsChart.options.plugins.legend.labels.color = newTextColor;
                operationsChart.options.plugins.tooltip.backgroundColor = isDarkNow ? '#0f172a' : '#ffffff';
                operationsChart.options.plugins.tooltip.titleColor = isDarkNow ? '#ffffff' : '#0f172a';
                operationsChart.options.plugins.tooltip.bodyColor = isDarkNow ? '#cbd5e1' : '#475569';
                
                operationsChart.update();
            }, 100);
        });
    }
});
