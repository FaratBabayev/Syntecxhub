package com.example.encryptedandroidchat
import java.io.InputStream
import java.io.OutputStream
import java.net.Socket
class SocketManager {
    private lateinit var socket: Socket
    private lateinit var input: InputStream
    private lateinit var output: OutputStream
    fun connect(host: String, port: Int, username: String) {
        socket = Socket(host, port)
        input = socket.getInputStream()
        output = socket.getOutputStream()
        // Send username
        output.write(username.toByteArray())
        output.flush()
    }
    fun sendMessage(data: ByteArray) {
        output.write(data)
        output.flush()
    }
    fun receiveMessages(onMessageReceived: (ByteArray) -> Unit) {
        Thread {
            val buffer = ByteArray(1024)
            while (true) {
                val bytesRead = input.read(buffer)
                if (bytesRead == -1) break
                val message = buffer.copyOf(bytesRead)
                onMessageReceived(message)
            }
        }.start()
    }
    fun disconnect() {
        socket.close()
    }
}