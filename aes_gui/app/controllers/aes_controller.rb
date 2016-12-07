class AesController < ApplicationController
  def home
  end

  def upload
  	uploaded_io = params[:file]
  	File.open(Rails.root.join('public', 'uploads', uploaded_io.original_filename), 'wb') do |file|
  		file.write(uploaded_io.read)
  	end

  	if !params[:iv].nil?
  		result = `python3 lib/assets/aes/driver.py #{params[:type]} #{uploaded_io.original_filename} #{params[:mode]} #{params[:key]} #{params[:iv]}`
  	else
  		result = `python3 lib/assets/aes/driver.py #{params[:type]} #{uploaded_io.original_filename} #{params[:mode]} #{params[:key]}`
  	end

  	file = File.read(Rails.root.join('public', 'uploads', uploaded_io.original_filename))

  	`rm #{Rails.root.join('public', 'uploads', uploaded_io.original_filename)}`

  	send_data file, :filename => uploaded_io.original_filename
  end

end