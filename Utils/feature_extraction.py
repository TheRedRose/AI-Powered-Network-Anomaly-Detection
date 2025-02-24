def extract_features(packet):
    return [
        len(packet),               # Feature 1: Packet size
        packet.time,               # Feature 2: Timestamp
        packet.ttl if "IP" in packet else 0,  # Feature 3: TTL
        packet.sport if "TCP" in packet or "UDP" in packet else 0,  # Feature 4: Source Port
        packet.dport if "TCP" in packet or "UDP" in packet else 0   # Feature 5: Destination Port
    ]