// Tout le js des graphs
// https://towardsdatascience.com/flask-and-chart-js-tutorial-i-d33e05fba845

var races = 
const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'radar',
    data: {
        labels: races,
        datasets: [{
            label: 'Distribution des races',
            data: [20, 40, 60, 80, 100, 120, 140,],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)'
            ],
            borderColor: [
                'rgb(255, 255, 255)',
            ],
            Color: [
                'rgb(255,255,255)',
            ],

            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

