## Modality-to-Economic-Object Map

| Modality | Typical raw object | Latent economic object | Common extraction strategy | Main risk |
|---|---|---|---|---|
| Text | Job ads, filings, contracts, policy text, news, open-ended surveys | tasks, rules, risk, policy content, beliefs, narratives | dictionaries, supervised classification, topic models, embeddings | semantic drift, strategic language, label leakage |
| Images | satellite imagery, street-view, scans, screenshots | poverty, urban activity, built environment, environmental exposure | convolutional nets, transfer learning, image embeddings | proxy instability, domain mismatch, omitted physical context |
| Audio | speeches, interviews, calls, recordings | tone, emotion, stress, fluency, disclosure | acoustic features, speech embeddings, supervised audio classification | identity contamination, recording quality, context sensitivity |
| Video | interviews, workplace footage, meetings, multimodal records | interaction quality, sequence, gesture, task execution | multimodal classification, vision-language models, manual coding + ML | high labeling burden, privacy, unclear economic mapping |
| Multimodal | combined text-image-audio-video inputs | complex institutional or behavioral states | late fusion, joint embeddings, multimodal transformers | interpretability, drift, modality imbalance |
