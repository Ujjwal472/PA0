from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
	if request.method == 'POST':
		input_text = request.form['input_text'].strip()
		transformed_text = ''
		# Encryption algorithm goes here!

		for c in input_text: # We iterate through each character of the input string
			# checking if the current character is lower-cased.
			if ord(c) >= ord('a') and ord(c) <= ord('z'):
				# Performing the operations as mentioned in the algorithm in a single step
				transformed_text += chr(2 * ord('a') + 25 - ord(c))

			# checking if the current character is lower-cased.
			elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
				transformed_text += chr(2 * ord('A') + 25 - ord(c))

			# Nothing to be done in case of white space.
			elif c == ' ':
				transformed_text += ' '
				continue

			# Rest all the characters are added as it is to the cipher text.
			else:
				transformed_text += c

		# Encryption algorithm ends here
		return render_template('result.html', result={'orig':input_text, 'result':transformed_text})

if __name__ == '__main__':
	app.run()