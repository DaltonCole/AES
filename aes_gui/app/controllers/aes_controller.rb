class AesController < ApplicationController
  def home
  end

  def upload
  	puts(params[:mode])

  	if params[:type] != 'Encrypt' and params[:type] != 'Decrypt'
  		flash[:notice] = "Please specify Encrypt or Decrypt"
  		redirect_to '/'
  	elsif params[:file] == '' or params[:file].nil?
  		flash[:notice] = "Please input a file"
  		redirect_to '/'
  	elsif params[:mode] != 'ECB' and params[:mode] != 'CBC'
  		flash[:notice] = "Please select a mode"
  		redirect_to '/'
  	elsif params[:key] == ''
  		flash[:notice] = "Please input a key"
  		redirect_to '/'
  	elsif params[:key].length != 16 and params[:key].length != 24 and params[:key].length != 32
  		flash[:notice] = "Please select a key size of either length 16, 24, or 32 characters"
  		redirect_to '/'
  	elsif params[:iv] == '' and params[:mode] == 'CBC'
  		flash[:notice] = "Please input an IV if using CBC mode"
  		redirect_to '/'
  	elsif params[:iv] != '' and params[:iv].length != 16
  		flash[:notice] = "Please enter an IV of length 16 characters"
  		redirect_to '/'
  	else
	  	uploaded_io = params[:file]
	  	File.open(Rails.root.join('public', 'uploads', uploaded_io.original_filename), 'wb') do |file|
	  		file.write(uploaded_io.read)
	  	end

      File.open(Rails.root.join('public', 'uploads', uploaded_io.original_filename + '.txt'), 'wb') do |file|
        file.write(params[:type] + "\n")
        file.write(uploaded_io.original_filename + "\n")
        file.write(params[:mode] + "\n")
        file.write(params[:key] + "\n")
        if !params[:iv].nil?
          file.write(params[:iv] + "\n")
        end
      end

      result = `python3 lib/assets/aes/driver.py < "#{Rails.root.join('public', 'uploads', uploaded_io.original_filename + '.txt')}"`

	  	file = File.read(Rails.root.join('public', 'uploads', uploaded_io.original_filename))

	  	`rm "#{Rails.root.join('public', 'uploads', uploaded_io.original_filename)}"`
      `rm "#{Rails.root.join('public', 'uploads', uploaded_io.original_filename + '.txt')}"`

	  	send_data file, :filename => params[:output_file]
    end
  end
end