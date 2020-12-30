# Introduction to the Paillier cryptosystem

## What is the Paillier cryptosystem?

In this section you will learn about the Paillier cryptosystem, which was published in 1999. This is a _partial homomorphic encryption scheme_ based on _public key cryptography_ and _modular arithmetic_.

This is an additive homorphic cryptosystem, which basically means that we can add encrypted integers together. More specifically, the process looks like this:

1. Alice generates a private/public key pair.
1. Anybody can encrypt an integer under Alice’s public key, and Alice can use her private key to decrypt such ciphertexts.
1. Given Alice‘s public key and two ciphertexts, anybody can compute an encrypted output which will decrypt to the result of adding those two integers together.
1. In a similar fashion, we can also perform multiplication of an encrypted integer by a plaintext integer.

In the rest of this section we will cover:

1. Key generation
1. Encryption and decryption (with a worked example)
1. Homomorphic addition and multiplication (with a worked example)

### QUIZ

1.  Which type of homomorphic encryption scheme is the Paillier cryptosystem?

    -   Partial (correct)
    -   Somewhat
    -   Fully

1.  Which homomorphic operations are possible using the Paillier cryptosystem?

    -   Addition of two ciphertexts (correct)
    -   Multiplication of two ciphertexts
    -   Addition of a ciphertext and a plaintext (possible by encrypting the plaintext first)
    -   Multiplication of a ciphertext and a plaintext (correct)

## Key generation

We will use a few helper functions:

1. $$gcd(x, y)$$ outputs the greatest common divisor of $$x$$ and $$y$$.
1. $$lcm(x, y)$$ outputs the least common multiple of $$x$$ and $$y$$.
1. $$L(n, x) = \frac{x - 1}{n}$$.

Then key generation works as follows:

1. Pick two large prime numbers $$p$$ and $$q$$, randomly and in dependently. Confirm that $$\mathrm{gcd}(pq, (p-1)(q-1))$$ is $$1$$. If not, start again.
1. Compute $$n = pq$$.
1. Compute $$\lambda$$ as $$\mathrm{lcm}(p-1, q-1)$$.
1. Pick a random integer $$g$$ in the set $$\mathbb{Z}^*_{n^2}$$ (integers between $$1$$ and $$n^2$$).
1. Calculate the [modular multiplicative inverse][modular multiplicative inverse wiki] $$\mu = (L(n, g^\lambda \mod n^2))^{-1} \mod n$$. If $$\mu$$ does not exist, start again from step 1.
1. The public key is $$(n, g)$$. Use this for encryption.
1. The private key is $$\lambda$$. Use this for decryption.

[modular multiplicative inverse wiki]: https://en.wikipedia.org/wiki/Modular_multiplicative_inverse

## Encryption and decryption

The basic intuition behind encryption with the Paillier cryptosystem is that we are taking a number in the range $$[0, n)$$ and hiding it in the much larger range $$[0, n^2)$$.

Encryption can work for any $$m$$ in the range $$0 \leq m < n$$:

1. Pick a random number $$r$$ in the range $$0 < r < n$$.
1. Compute ciphertext $$c = g^m \cdot r^n \mod n^2$$.

Decryption presupposes a ciphertext created by the above encryption process, so that $$c$$ is in the range $$0 < c < n^2$$:

1. Compute the plaintext $$m = L(n, c^\lambda \mod n^2) \cdot \mu \mod n$$.

(Reminder: we can always recalculate $$\mu$$ from $$\lambda$$ and the public key).

!!! WORKED EXAMPLE

### QUIZ

1.  What constitutes the private key in the Paillier cryptosystem?

    -   lambda (correct)
    -   mu (can be derived from n, g and lambda)
    -   n
    -   g

1.  What constitutes the public key in the Paillier cryptosystem?

    -   lambda
    -   mu
    -   n (correct)
    -   g (correct)

1.  What is the modulus for plaintexts in the Paillier cryptosystem?

    -   n (correct)
    -   n^2
    -   p
    -   q

1.  What is the modulus for ciphertexts in the Paillier cryptosystem?

    -   n
    -   n^2 (correct)
    -   p
    -   q

## Homomorphic addition and multiplication

Let’s take a look at the homomorphic properties of this encryption scheme…

When two ciphertexts are multiplied, the result decrypts to the sum of their plaintexts:

$$
D_{priv}(E_{pub}(m_1) \cdot E_{pub}(m_2) \mod n^2) = m_1 + m_2 \mod n
$$

When a ciphertext is raised to the power of a plaintext, the result decrypts to the product of the two plaintexts:

$$
D_{priv}(E_{pub}(m_1)^{m_2} \mod n^2) = m_1 \cdot m_2 \mod n
$$

(Note that this result is just a special case of homomorphic addition, where we add the same encrypted number to itself a certain number of times.)

### Gotchas

There are a couple of special cases which need to be handled carefully. The first is multiplying by $$0$$. Because any number to the power of $$0$$ is $$1$$, if we multiply a ciphertext by a plaintext $$0$$ using the method above, the result will always be $$1$$, and anyone who sees this "encrypted" value will know that it decrypts to $$0$$. Luckily we can use an alternative method for this case. Multiplying any number by $$0$$ gives $$0$$, which means we can just skip the calculations and encrypt a $$0$$ directly using the standard public key encryption scheme. Since encryption step introduces a random number, nobody without the private key will be able to know what the plaintext is.

The other case is multiplying by $$1$$. Because any number $$x$$ to the power of $$1$$ is $$x$$, if we multiply a ciphertext by a plaintext $$1$$ using the normal method, the output will be the same as the input. This is less severe than the case with $$0$$ where the encrypted value could be inferred, but still a problem because anybody who is watching the communication between whoever holds the private key and whoever is multiplying numbers will be able to work out that the number was multiplied by $$1$$. The solution here is another workaround: instead of multiplying by $$1$$, we perform an equivalent operation: adding $$0$$! We just freshly encrypt a $$0$$ and perform the usual addition procedure to obtain a secure ciphertext.

### QUIZ

1.  Which cases have to be handled with care when implementing the Paillier cryptosystem?

    -   Adding 0
    -   Adding 1
    -   Adding a number to itself
    -   Multiplying by 0 (correct)
    -   Multiplying by 1 (correct)
    -   Multiplying by $$\lambda$$
