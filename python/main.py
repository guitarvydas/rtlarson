import generated

[palette, env] = generated.initialize ()

generated.delay_install (palette)
generated.count_install (palette)
generated.reverser_install (palette)
generated.decode_install (palette)
generated.monitor_install (palette)

generated.start (palette, env)
