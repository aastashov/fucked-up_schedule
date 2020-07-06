window.chartColors = {
  name1: "rgb(54, 162, 235, 1)",  // set name
  new_cases: "rgb(75, 192, 192, 1)",
  name2: "rgb(201, 203, 207, 1)",  // set name
  name3: "rgb(255, 159, 64, 1)",  // set name
  name4: "rgb(153, 102, 255, 1)",  // set name
  new_deaths: "rgb(255, 99, 132, 1)",
  name5: "rgb(255, 205, 86, 1)",  // set name
};

let c = null;
let c2 = [];

function loadChartData(country, labels, dataset) {
  const ctx = document.getElementById('myChart').getContext('2d');
  let datasets = [];
  for (let i = 0; i < dataset.length; i++) {
    let data = dataset[i];
    datasets.push(
      {
        label: data.ru,
        backgroundColor: window.chartColors[data.name],
        borderColor: window.chartColors[data.name].replace('1)', '0.5)'),
        data: data.data,
        fill: false,
      }
    );
  }

  const config = {
    type: 'line',
    data: {
      labels: labels,
      datasets: datasets,
    },
    options: {
      responsive: true,
      title: {
        display: true,
        text: country,
      },
      tooltips: {
        mode: 'index',
        intersect: false,
      },
      hover: {
        mode: 'nearest',
        intersect: true
      },
      scales: {
        xAxes: [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Day'
          }
        }],
        yAxes: [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Value'
          }
        }]
      }
    }
  };
  const chart = new Chart(ctx, config);
}
