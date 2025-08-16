// const express = require('express');
// const http = require('http');
// const { Server } = require('socket.io');
// const { exec } = require('child_process');
// const path = require('path');
// const cors = require('cors'); // Import CORS

// const app = express();
// const server = http.createServer(app);

// // Enable CORS for all routes
// app.use(cors({
//     origin: 'http://127.0.0.1:5000', // Allow requests from this origin
//     methods: ['GET', 'POST'], // Allow only specific HTTP methods
//     credentials: true // Allow cookies and credentials
// }));

// const io = new Server(server, {
//     cors: {
//         origin: 'http://127.0.0.1:5000', // Allow Socket.IO connections from this origin
//         methods: ['GET', 'POST']
//     }
// });

// // Serve static files from the "public" directory (if needed)
// app.use(express.static(path.join('website', 'public')));

// io.on('connection', (socket) => {
//     console.log('A user connected');

//     socket.on('start_detection', () => {
//         // Run the YOLOv9 detection script
//         const yoloProcess = exec('python ../yolov9/detect_dual.py --weights ../yolov9/yolov9-c.pt --conf 0.5 --source 0 --device 0', (error, stdout, stderr) => {
//             if (error) {
//                 console.error(`exec error: ${error}`);
//                 return;
//             }
//             console.log(`stdout: ${stdout}`);
//           //  console.error(`stderr: ${stderr}`);
//         });

//         yoloProcess.stdout.on('data', (data) => {
//             // Send detection results to the frontend
//             socket.emit('detection_result', data.toString());
//             console.log(`Emitting detection result: ${data.toString()}`);


//         });
        


//         yoloProcess.stderr.on('data', (data) => {
//             console.error(`stderr: ${data}`);
//         });
//     });

//     socket.on('connect', () => {
//         console.log('#################  Connected to server');
//     });

//     socket.on('disconnect', () => {
//         console.log('User disconnected');
//     });
// });

// server.listen(3000, () => {
//     console.log('Server is running on http://localhost:5000');
// });


