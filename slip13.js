var http=require('http');
var fs=require('fs');
var formidable=require('formidable');
var mysql=require('mysql');


var con=mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"",
    database: "studentdb"
});


http.createServer(function(req,res){
    if(req.url=='/'){
        res.writeHead(200, {'content-Type':'text/html'});
        res.write('<form action="fapp" method="post" enctype="multipart/form-data">');
        res.write('<h1>Registration Form</h1><br>');
        res.write('User Name : <input type="text" name="t1"><br>');
        res.write('Password : <input type="text" name="t2"><br>');
        res.write('<input type="button" value="LOGIN"><br>');
        res.end();
        
    }
    else if(req.url=='/fapp'){
        var form=new formidable.IncomingForm();
        form.parse(req, function(err,fields,files){
            var un=fields.t1;
            var pass=fields.t2;
            res.write('<h1><center>Hello : ' + un + '</center></h1><br>');
            con.connect(function(err){
                if(!err){
                    con.query("SELECT * FROM login where uname = ? and password = ?" , [un, pass], function(err,result,fields){
                        if(result.length>0){
                            res.end('<h1>LOGIN SUCCESS</h1>');
                        }
                        else{
                            res.end('<h1>User Name and Password not matching</h1>');
                        }
                    });
                }
            });
        });
    }
    else{
        res.end("Page Not Found");
    }
}).listen(3000);

