Is there something I can do to make this code:

(with-open-file (json-stream "~/projects/rtlarson/eyeballs.json" :direction :input)
  (json:decode-json json-stream))

inhale this eyeballs.json without choking?

            {
                "name": "\ud83d\udca1",
                "id": 26
            },

