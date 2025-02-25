const express = require('express');
const path = require('path');
const app = express();
const port = 3015;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/app', (req, res) => {
    res.render('app/index', { title: 'Loading...' });
  });
  

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
