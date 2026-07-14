package com.example.encryptedandroidchat

import android.graphics.Color
import android.view.Gravity
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.LinearLayout
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class ChatAdapter(
    private val messages: MutableList<Message>
) : RecyclerView.Adapter<ChatAdapter.MessageViewHolder>() {

    class MessageViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {

        val tvMessage: TextView = itemView.findViewById(R.id.tvMessage)

        val container: LinearLayout =
            itemView.findViewById(R.id.messageContainer)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MessageViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_message, parent, false)

        return MessageViewHolder(view)
    }

    override fun onBindViewHolder(holder: MessageViewHolder, position: Int) {

        val message = messages[position]

        holder.tvMessage.text = message.text

        if (message.isSentByMe) {
            holder.tvMessage.setBackgroundResource(R.drawable.bg_message_sent)
            holder.tvMessage.setTextColor(Color.WHITE)
            holder.container.gravity = Gravity.END
        } else {
            holder.tvMessage.setBackgroundResource(R.drawable.bg_message_received)
            holder.tvMessage.setTextColor(Color.BLACK)
            holder.container.gravity = Gravity.START
        }
    }

    override fun getItemCount(): Int = messages.size
}