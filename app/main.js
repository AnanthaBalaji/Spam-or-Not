const {app,BrowserWindow} = require('electron')
const axios = require('axios')

createWindow=()=>{
    let win = new BrowserWindow({
        width:900,
        height:600,
        resizable: false,
        autoHideMenuBar: true,
        webPreferences:{
            nodeIntegration:true
        }
    })
    win.loadFile('index.html')
}

app.on('ready',createWindow)