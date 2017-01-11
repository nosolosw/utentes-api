'use strict';

const electron = require('electron');
// Module to control application life.
const app = electron.app;
// Module to create native browser window.
const BrowserWindow = electron.BrowserWindow;

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow,
  splashWindow;

function createWindow (mainAddr, subpy) {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 1600,
    height: 1200,
    minWidth: 1152,
    minHeight: 864,
    "webPreferences": {"nodeIntegration": true},
    title: 'Gestão de Utentes',
    show: false,
    icon: __dirname + '/sixhiara_256.ico',
  });
  mainWindow.maximize();

  mainWindow.loadURL(mainAddr, {"extraHeaders" : "pragma: no-cache\n"});
  // mainWindow.webContents.reloadIgnoringCache();
  mainWindow.webContents.session.clearCache(function(){console.log('Cache cleared')});
  mainWindow.webContents.session.clearStorageData(function(){console.log('StorageData cleared')});
  // mainWindow.webContents.openDevTools();

  mainWindow.webContents.once('did-finish-load', function() {
    mainWindow.show();
    splashWindow.close();
  });


  mainWindow.on('close', function() {
    mainWindow.webContents.session.clearCache(function(){console.log('Closed: Cache cleared')});
    mainWindow.webContents.session.clearStorageData(function(){console.log('Closed: StorageData cleared')});
  });

  mainWindow.on('closed', function() {
    mainWindow = null;
    subpy.kill('SIGINT');
  });

}

// process.on('uncaughtException', function(err){
//   console.log(err);
//   for (i in err) {
//     console.log(err[i]);
//   }
// });

app.on('ready', function() {
  // console.log(app.getPath('userData'));

  showSplash();

  var spawn = require('child_process').spawn;
  var subpy = spawn('./Python27/python', ['./Python27/Scripts/pserve-script.py',  './utentes-api/production.ini']);
  // var subpy = spawn('../../virtualenvs/sixhiara/bin/pserve', ['production.ini']);

  setTimeout(function(){
    var mainAddr = 'http://localhost:6543/static/utentes-ui/exploracao-search.html';
    createWindow(mainAddr, subpy);
  }, 4000);

});

function showSplash() {
  splashWindow = new BrowserWindow({
    useContentSize: true,
    width: 400,
    height: 400,
    center: true,
    frame: false,
    type: 'splash',
  });
  splashWindow.on('closed', function() {
    splashWindow = null;
  });
  splashWindow.loadURL('file://' + __dirname + '/splash.html');
}

// Quit when all windows are closed.
app.on('window-all-closed', function () {
  // On OS X it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', function () {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (mainWindow === null) {
    console.log('This should not happen');
    createWindow();
  }
});
