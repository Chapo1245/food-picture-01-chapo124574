# Best-Looking Food Picture — make.fun entry (food-picture-01)

A hand lifting a margherita pizza slice, long molten mozzarella strands
pulling from the slice, blistered leopard-spotted crust, glossy San Marzano
sauce, fresh basil and an olive-oil drizzle, oven embers glowing behind.
One clear focal point filling the frame, warm dramatic light — it reads
clearly even small.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` (JPEG bytes, 1024x683, 169107 bytes) to
`/output/entry.png`. No network, no randomness, no clock — two runs
write exactly the same bytes.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
ls -l out/entry.png
```

## License

MIT — see `LICENSE`.
