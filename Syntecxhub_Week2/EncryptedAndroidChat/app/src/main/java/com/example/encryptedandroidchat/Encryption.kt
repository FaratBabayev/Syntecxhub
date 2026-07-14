package com.example.encryptedandroidchat
import java.security.SecureRandom
import javax.crypto.Cipher
import javax.crypto.spec.GCMParameterSpec
import javax.crypto.spec.SecretKeySpec
object Encryption {
    private const val AES_MODE = "AES/GCM/NoPadding"
    private const val IV_SIZE = 12
    private const val TAG_SIZE = 128
    // Same key for both clients (16 bytes = AES-128)
    private val SECRET_KEY = "12345678901234567890123456789012".toByteArray()
    fun encrypt(message: String): ByteArray {
        val cipher = Cipher.getInstance(AES_MODE)
        val iv = ByteArray(IV_SIZE)
        SecureRandom().nextBytes(iv)
        val key = SecretKeySpec(SECRET_KEY, "AES")
        cipher.init(
            Cipher.ENCRYPT_MODE,
            key,
            GCMParameterSpec(TAG_SIZE, iv)
        )
        val encrypted = cipher.doFinal(message.toByteArray())
        return iv + encrypted
    }
    fun decrypt(data: ByteArray): String {
        val iv = data.copyOfRange(0, IV_SIZE)
        val encrypted = data.copyOfRange(IV_SIZE, data.size)
        val cipher = Cipher.getInstance(AES_MODE)
        val key = SecretKeySpec(SECRET_KEY, "AES")
        cipher.init(
            Cipher.DECRYPT_MODE,
            key,
            GCMParameterSpec(TAG_SIZE, iv)
        )
        return String(cipher.doFinal(encrypted))
    }
}