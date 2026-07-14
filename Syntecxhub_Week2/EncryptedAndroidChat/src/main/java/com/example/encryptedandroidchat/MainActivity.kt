package com.example.encryptedandroidchat
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
class MainActivity : AppCompatActivity() {
    private lateinit var rvMessages: RecyclerView
    private lateinit var etMessage: EditText
    private lateinit var btnSend: Button
    private lateinit var chatAdapter: ChatAdapter
    private val messages = mutableListOf<Message>()
    private val socketManager = SocketManager()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        rvMessages = findViewById(R.id.recyclerViewMessages)
        etMessage = findViewById(R.id.etMessage)
        btnSend = findViewById(R.id.btnSend)
        chatAdapter = ChatAdapter(messages)
        rvMessages.layoutManager = LinearLayoutManager(this)
        rvMessages.adapter = chatAdapter
        Thread {
            try {
                socketManager.connect(
                    Constants.HOST,
                    Constants.PORT,
                    Constants.USERNAME
                )
                socketManager.receiveMessages { encryptedData ->
                    try {
                        val decrypted =
                            Encryption.decrypt(encryptedData)
                        runOnUiThread {
                            messages.add(
                                Message(
                                    decrypted,
                                    false
                                )
                            )
                            chatAdapter.notifyItemInserted(
                                messages.size - 1
                            )
                            rvMessages.scrollToPosition(
                                messages.size - 1
                            )
                        }
                    } catch (e: Exception) {
                        e.printStackTrace()
                    }
                }
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }.start()
        btnSend.setOnClickListener {
            val text = etMessage.text.toString()
            if(text.isNotEmpty()) {
                messages.add(
                    Message(
                        text,
                        true
                    )
                )
                chatAdapter.notifyItemInserted(
                    messages.size - 1
                )
                Thread {
                    try {
                        val encrypted =
                            Encryption.encrypt(text)
                        socketManager.sendMessage(
                            encrypted
                        )
                    } catch(e: Exception) {
                        e.printStackTrace()
                    }
                }.start()
                etMessage.text.clear()
            }
        }
    }
    override fun onDestroy() {
        super.onDestroy()
        socketManager.disconnect()
    }
}