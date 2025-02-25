import express from "express"
import path from "path"
import OpenAI from "openai";
import { fileURLToPath } from 'url';
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const port = 3015;



const API_KEY = "sk-proj-<=== API KEY ===>"
const model = "gpt-4o-mini"
const openai = new OpenAI({"apiKey": API_KEY});

app.use(express.json()); // Parse JSON bodies

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/app', (req, res) => {
    res.render('app/index', { title: 'Loading...' });
});

app.post('/app', (req, res) => {
    console.log(req.body);
    openai.chat.completions.create({
        model,
        store: true,
        messages: [
            {"role": "developer", "content": `
              Either answer the user question or give him python code to solve his task. He currently is inside
              the directory ${req.body.dir}. Only use absolute paths in your python code. Store any potential result in a variable named "result"
              and they will be given back to you. Do not log things, give at most one code block per message. The user doesn't care about python specifically, but only the programms and outcomes.
              Make every code block you send fully self-contained, including the import statements.
            `},
            ...req.body.messages
        ]
    }).then(r => {
        const gpt_msg = r.choices[0].message.content;
        if (gpt_msg.includes("```python")){
            res.json({
              "answer_type": "execute",
              "text": gpt_msg
            });
            return;
        }
        
        res.json({
          "answer_type": "text",
          "text": gpt_msg
        });
    });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
