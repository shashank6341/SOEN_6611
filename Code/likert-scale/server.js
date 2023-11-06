const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const mysql = require('mysql2');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Serve static files (e.g., HTML, CSS, JavaScript) from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

const dbConfig = {
  host: 'localhost',
  user: 'root',
  password: 'root123',
  database: 'mydb',
};

const db = mysql.createConnection(dbConfig);

db.connect((err) => {
  if (err) {
    console.error('Error connecting to MySQL:', err);
  } else {
    console.log('Connected to MySQL database');
  }
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Handle form submissions to store survey data
// Handle form submissions to store survey data and calculate the average
app.post('/submit-survey', (req, res) => {
    const surveyResponse = req.body;
  
    // Insert the survey data into the MySQL database
    const query = 'INSERT INTO surveydata (q1, q2, q3, q4, q5, q6, q7) VALUES (?, ?, ?, ?, ?, ?, ?)';
    const values = [
      surveyResponse.q1,
      surveyResponse.q2,
      surveyResponse.q3,
      surveyResponse.q4,
      surveyResponse.q5,
      surveyResponse.q6,
      surveyResponse.q7,
    ];
  
    // Calculate the average of the 7 questions and store it in the 'score' column
    const averageQuery = 'UPDATE surveydata SET score = (q1 + q2 + q3 + q4 + q5 + q6 + q7) / 7';
  
    db.query(query, values, (err, result) => {
      if (err) {
        console.error('Error inserting survey data:', err);
        res.status(500).json({ message: 'Internal server error' });
      } else {
        console.log('Survey data inserted:', result.insertId);
        
        // Calculate the average immediately after inserting the data
        db.query(averageQuery, (avgErr, avgResult) => {
          if (avgErr) {
            console.error('Error calculating the average:', avgErr);
            res.status(500).json({ message: 'Internal server error' });
          } else {
            console.log('Average calculated and stored in the "score" column.');
            res.json({ message: 'Survey data submitted successfully' });
          }
        });
      }
    });
  });
  

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
