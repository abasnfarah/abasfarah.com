// Taking in express
var express = require("express");
var app = express();
var router = express.Router();


// Path for files up
var path = __dirname + "/views";


router.use(function(req,res,next) {
	console.log("/" + req.method);
	next();
});

router.get("/",function(req,res) {
	res.sendFile(path + "/LandingPage.html");
});

router.get("/LandingPage",function(req,res) {
	res.sendFile(path + "/LandingPage.html");
});

app.use(express.static(__dirname + "/public"));

app.use("/",router);

app.use("*",function(req,res) {
	res.sendFile(path + "/404.html");
});

app.listen(8080,function() {
	console.log("live on port 8080")
})


