var data = [
  	{
	    y: ['HTML', 'CSS', 'Python', 'Django', 'React', 'React Native', 'Visualization'],
	    x: [96, 60, 80, 90, 50, 40, 65],
	    type: 'bar',
	    marker: {
		    color: 'orangered'
		},
		width: [0.2,0.2,0.2,0.2,0.2,0.2, 0.2],
		orientation: 'h',
    }
];

var layout = {
  	title: 'Skills Visualization', 
	yaxis:{
		title: 'Skills'
	},
	xaxis:{
		title: 'Fluency in Percentage (%)'
	}
}

Plotly.newPlot('skill-graphs', data, layout);