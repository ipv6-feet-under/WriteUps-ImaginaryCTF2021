![ImaginaryCTF](../../banner.png)

# Cookie Stream

|Author|Points|Category|Solves|
|---|---|---|---|
|Eth007|150|Web|86|

### Description

```
Cookie streaming service? Naaaaaaah. Password protected Rickroll as a Service? YAAAAAAAAAAAAAAAAAAAAAAAAAAAASSSSSSSSSSS!	
```

### Attachments

* [app.py](app.py)
* http://cookie-stream.chal.imaginaryctf.org/

Visiting the website we get a login page:

![login.PNG](login.PNG)

Trying some random cred's we get to http://cookie-stream.chal.imaginaryctf.org/backend with `Wrong username/password.`

So let's take a look at the [app.py](app.py).
Right at the beginning we find usernames and corresponding hashes:
```py
users = {
    'admin' : '240964a7a2f1b057b898ef33c187f2c2412aa4d849ac1a920774fd317000d33ebb8b0064834ed1f8a74763df4e95cd8c8be3a154b46929c3969ce323db69b81f',
    'ImaginaryCTFUser' : '87197acc4657e9adcc2e4e24c77268fa5b95dea2867eacd493a0478a0c493420bfb2280c7e4e579a604e0a243f74a36a8931edf71b088add09537e54b11ce326',
    'Eth007' : '444c67bb7d9d56580e0a2fd1ad00c535e465fc3ca9558e8333512fe65ff971a3dfb6b08f48ea4f91f8e8b55887ec3f0d7634a8df98e636a4134628c95a8f0ebf',
    'just_a_normal_user' : 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86',
    'firepwny' : '6adee5baa5ad468ac371d40771cf2e83e3033f91076f158d2c8d5d7be299adfce15247067740edd428ef596006d6eaa843b36cc109618e0a1cae843b6eed5c29',
    ':roocursion:' : '7f5310d2675c09c1b274f7642bf4979b2ce642515551a7617d155033e77ecfd53dede33ee541adde2f1072739696d0138d1b2f90c9ecc596095fa43b759e9baa',
}
```
With [CrackStation](https://crackstation.net/) we get at least some of the passwords:
```
ImaginaryCTFUser:idk
Eth007:supersecure
just_a_normal_user:password
firepwny:pwned
```
With all of the accounts above we get:

![logged_in.PNG](logged_in.PNG)

The hint tells us that we have to login with the admin credentials but the hash of the admin wasn't in the database of [CrackStation](https://crackstation.net/).
The source code [app.py](app.py) tells us that there is a cookie `auth` generated:
```py
@app.route('/backend', methods=['GET', 'POST'])
def backend():
    if request.method == 'POST':
        if not check(request.form['username'], request.form['password']):
            return 'Wrong username/password.'
        resp = make_response(redirect('/home'))
        nonce = urandom(8)
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce) # my friend told me that cbc had some weird bit flipping attack? ctr sounds way cooler anyways
        cookie = hexlify(nonce + cipher.encrypt(pad(request.form['username'].encode(), 16)))
        resp.set_cookie('auth', cookie)
        return resp
    else:
        return make_response(redirect('/home'))
```



There is our flag:
```
ictf{d0nt_r3us3_k3ystr34ms_b72bfd21}
```