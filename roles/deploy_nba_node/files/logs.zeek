redef LogAscii::use_json=T;

event zeek_init(){
  #Log::disable_stream(Conn::LOG);
  #Log::disable_stream(Files::LOG);
  #Log::disable_stream(Weird::LOG);
  #Log::disable_stream(SSH::LOG);
  #Log::disable_stream(DCE_RPC::LOG);
  #Log::disable_stream(DHCP::LOG);
  #Log::disable_stream(SIP::LOG);
  #Log::disable_stream(FTP::LOG);
  #Log::disable_stream(NTLM::LOG);
  #Log::disable_stream(RDP::LOG);
  #Log::disable_stream(SNMP::LOG);
  #Log::disable_stream(SOCKS::LOG);
  Log::disable_stream(Syslog::LOG);
  #Log::disable_stream(Tunnel::LOG);
  #Log::disable_stream(KRB::LOG);
  #Log::disable_stream(DPD::LOG);
  #Log::disable_stream(Notice::LOG);
  Log::disable_stream(PacketFilter::LOG);
  #Log::disable_stream(PE::LOG);
  #Log::disable_stream(CaptureLoss::LOG);
  #Log::disable_stream(HTTP::LOG);
  #Log::disable_stream(Reporter::LOG);
  #Log::disable_stream(SSL::LOG);
  #Log::disable_stream(Stats::LOG);
  #Log::disable_stream(X509::LOG);
  #Log::disable_stream(SMTP::LOG);
  #Log::disable_stream(Software::LOG); 
  #Log::disable_stream(SMB::FILES_LOG);
  #Log::disable_stream(SMB::MAPPING_LOG);
  #Log::disable_stream(LoadedScripts::LOG);
  #Log::disable_stream(DNS::LOG);
}