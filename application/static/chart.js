function loadChartData(location, label, labels, raw_data) {
  const ctx = document.getElementById('myChart').getContext('2d');
  const config = {
			type: 'line',
			data: {
				labels: labels,
				datasets: [{
					label: label,
					backgroundColor: 'rgba(75, 192, 192, 0.2)',
					borderColor: 'rgba(75, 192, 192, 1)',
					data: raw_data,
					fill: false,
				},
				]
			},
			options: {
				responsive: true,
				title: {
					display: true,
					text: location
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
