import { Meteor } from 'meteor/meteor';

import {PythonShell} from 'python-shell'; 

Meteor.startup(() => {

});

Meteor.methods({

	// send phrase to python script
	async sendPhrase(phrase) {
		return new Promise((resolve, reject) => {
			let options = {
			  mode: 'text',
			  pythonOptions: ['-u'], // get print results in real-time
			  scriptPath: '/Users/mikezhu/Desktop/hackathing1/',
			  args: ['this is a flitz ']
			};
			let results;
			PythonShell.run('cs98_milestone1.py', options, function (err, res) {
		  		if (err) throw err;
		  		console.log('results: %j', res);
		  		results = res;
			});
			resolve(results)
		});
	}
});
